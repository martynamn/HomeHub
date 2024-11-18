from operator import itemgetter

from django.db.models import Q
from django.http import JsonResponse
from pymongo import MongoClient
from django.conf import settings
from bson.objectid import ObjectId
from bson.json_util import dumps

from myapp.models import Property, Image, Address
from myapp.serializer import PropertySerializer, ImageSerializer, AddressSerializer
import base64
import json
import base64
from datetime import datetime

client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
db = client[settings.DATABASES['default']['NAME']]

def get_last_properties(number: int, user_id: str, ):
    properties = Property.objects.filter(Q(adType__in=['sale', 'rent']), userId=user_id)
    if not properties:
        return JsonResponse({'error': 'No properties found for this user'}, status=404)

    properties_list = PropertySerializer(properties, many=True).data
    properties_list.sort(key=itemgetter('creationDate'), reverse=True)

    last_properties = properties_list[:number]
    return JsonResponse(last_properties, safe=False)

def get_properties_by_user(user_id: str):
    properties = Property.objects.filter(userId=user_id)

    properties_list = PropertySerializer(properties, many=True).data
    return JsonResponse(properties_list, safe=False)

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
        address_id = db.ADDRESS.insert_one(address_data).inserted_id

        images = []
        for file in files:
            file_content = file.read()
            encoded_image = base64.b64encode(file_content).decode('utf-8')
            image_data = {
                'imageData': encoded_image,
                'filename': file.name
            }
            image_id = db.IMAGE.insert_one(image_data).inserted_id
            images.append(image_id)

        property_data = {
            'description': data.get('description'),
            'title': data.get('title'),
            'type': data.get('type'),
            'adType': data.get('adType'),
            'userId': data.get('userId'),
            'price': data.get('price'),
            'rooms': data.get('rooms'),
            'creationDate': datetime.now(),
            'address': address_id,
            'image': images[0] if images else None
        }
        property_id = db.PROPERTY.insert_one(property_data).inserted_id
        return {
            'success': True,
            'message': 'Property created successfully!',
            'property': str(property_id)
        }

    except Exception as e:
        return {'error': str(e)}