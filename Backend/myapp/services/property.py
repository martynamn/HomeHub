import base64
import json
import uuid
from datetime import datetime
from operator import itemgetter

from bson.objectid import ObjectId
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from pymongo import MongoClient

from myapp.models import Property
from myapp.serializer import PropertySerializer

client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
db = client[settings.DATABASES['default']['NAME']]


def get_last_properties(number: int, user_id: str, ):
    if not number:
        number = 3
    properties = Property.objects.filter(Q(adType__in=['sale', 'rent']), userId=user_id)
    if not properties:
        return JsonResponse({'error': 'No properties found for this user'}, status=404)

    properties_list = PropertySerializer(properties, many=True).data
    properties_list.sort(key=itemgetter('creationDate'), reverse=True)

    last_properties = properties_list[:number]
    return JsonResponse(last_properties, safe=False)


def get_properties_by_user(user_id: str):
    properties = Property.objects.filter(userId=user_id)
    if not properties:
        return JsonResponse({'error': 'No properties found for this user'}, status=404)

    properties_list = PropertySerializer(properties, many=True).data
    return JsonResponse(properties_list, safe=False)


def get_properties(request):
    filters = {
        "userId": request.GET.get("userId", None),
        "type": request.GET.get("type", None),
        "adType": request.GET.get("ad_type", None),
        "address__country": request.GET.get("country", None),
        "address__city": request.GET.get("city", None),
        "address__floor": int(request.GET.get("floor", )) if request.GET.get("floor", None) is not None else None,
        "rooms": int(request.GET.get("rooms", None)) if request.GET.get("rooms", None) is not None else None,
        "price__gte": int(request.GET.get("min_price", None)) if request.GET.get("min_price",
                                                                                 None) is not None else None,
        "price__lte": int(request.GET.get("max_price", None)) if request.GET.get("max_price",
                                                                                 None) is not None else None,
        "area__gte": int(request.GET.get("min_area", None)) if request.GET.get("min_area", None) is not None else None,
        "area__lte": int(request.GET.get("max_area", None)) if request.GET.get("max_area", None) is not None else None,
    }

    filters = {filter: value for filter, value in filters.items() if value is not None}

    q_filter = Q()
    for field, value in filters.items():
        if value is not None:
            q_filter &= Q(**{field: value})
    q_filter &= ~Q(adType="sold")

    properties = Property.objects.filter(q_filter)
    serialized_properties = PropertySerializer(get_paginated_properties(properties, request), many=True).data

    return JsonResponse(serialized_properties, safe=False)


def get_property(property_id: str):
    property = Property.objects.get(_id=property_id)
    if not property:
        return JsonResponse({'error': 'No property found'}, status=404)

    property_serialized = PropertySerializer(property).data
    return JsonResponse(property_serialized, safe=False)


def get_paginated_properties(properties, request):
    limit = request.GET.get('limit')
    index = request.GET.get('index')

    limit = int(limit) if limit is not None else 10
    index = int(index) if index is not None else 1

    paginator = Paginator(properties, limit)

    try:
        properties_page = paginator.page(index)
    except PageNotAnInteger:
        properties_page = paginator.page(1)
    except EmptyPage:
        properties_page = paginator.page(paginator.num_pages)

    return properties_page


def get_property_by_id(property_id):
    try:
        property_data = db.PROPERTY.find_one({'_id': ObjectId(property_id)})

        if not property_data:
            return {'error': 'Property not found'}

        address_data = db.ADDRESS.find_one({'_id': property_data['address']})
        property_data['address'] = address_data

        image_data = db.IMAGE.find_one({'_id': property_data['image']})
        property_data['image'] = image_data

        property_data['_id'] = str(property_data['_id'])
        property_data['address']['_id'] = str(property_data['address']['_id'])
        property_data['image']['_id'] = str(property_data['image']['_id'])

        return property_data

    except Exception as e:
        return {'error': str(e)}


def create_property(metadata, files):
    try:
        data = json.loads(metadata)

        address_data = {
            'country': data['address']['country'],
            'city': data['address']['city'],
            'postcode': data['address']['postcode'],
            'floor': data['address']['floor']
        }

        image_ids = []
        for file in files:
            file_content = file.read()
            encoded_image = base64.b64encode(file_content).decode('utf-8')

            image_id = str(uuid.uuid4())

            image_data = {
                '_id': image_id,
                'imageData': encoded_image,
                'filename': file.name,
                'uploadDate': datetime.now()
            }

            db.IMAGE.insert_one(image_data)
            image_ids.append(image_id)

        property_id = str(uuid.uuid4())

        property_data = {
            '_id': property_id,
            'description': data.get('description'),
            'title': data.get('title'),
            'type': data.get('type'),
            'adType': data.get('adType'),
            'userId': data.get('userId'),
            'price': data.get('price'),
            'rooms': data.get('rooms'),
            'creationDate': datetime.now(),
            'address': address_data,
            'images': image_ids
        }

        db.PROPERTY.insert_one(property_data)

        return {
            'success': True,
            'message': 'Property created successfully!',
            'property': property_id
        }

    except Exception as e:
        return {'error': str(e)}


def delete_property_by_id(property_id):
    try:
        result = db.PROPERTY.delete_one({'_id': property_id})

        if result.deleted_count == 0:
            return {'error': 'Property not found'}
        return {'success': True, 'message': 'Property deleted successfully'}

    except Exception as e:
        return {'error': str(e)}


def sold_property_by_id(property_id):
    try:
        result = db.PROPERTY.find_one_and_update(
            {'_id': property_id},
            {'$set': {'adType': 'sold'}},
            return_document=True
        )

        if result is None:
            return {'error': 'Property not found'}

        return {
            'success': True,
            'message': 'Property marked as sold successfully',
            'property_id': result['_id']
        }

    except Exception as e:
        return {'error': str(e)}


def update_property_by_id(property_id, metadata, files):
    try:
        property_data = create_property(metadata, files)
        result = db.PROPERTY.find_one_and_update(
            {'_id': property_id},
            {'$set': property_data},
            return_document=True
        )
        if result is None:
            return {'error': 'Property not found'}
        return {'success': True, 'message': 'Property updated successfully'}
    except Exception as e:
        return {'error': str(e)}
