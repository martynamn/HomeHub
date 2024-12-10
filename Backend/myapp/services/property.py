from operator import itemgetter

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from myapp.models import Property
from myapp.serializer import PropertySerializer


def get_last_properties(number: int, user_id: str, ):
    properties = Property.objects.filter(Q(adType__in=['sale', 'rent']), userId=user_id)
    if not properties:
        return JsonResponse({'error': 'No properties found for this user'}, status=404)

    properties_list = PropertySerializer(properties, many=True).data
    properties_list.sort(key=itemgetter('creationDate'), reverse=True)

    last_properties = properties_list[:number]
    return JsonResponse(last_properties, safe=False)


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
    property = Property.objects.get(_id = property_id)
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


def get_properties(request, user_id: str):
    filters = {
        "userId": user_id,
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
