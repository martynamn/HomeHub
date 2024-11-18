from django.http import JsonResponse
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['PROPERTY']
collection = db['PROPERTY']


def get_filter_parameters(request):
    ad_type = request.GET.get('ad_type')
    type = request.GET.get('type')
    country = request.GET.get('country')
    city = request.GET.get('city')
    floor = request.GET.get('floor')
    room = request.GET.get('room')
    user_id = request.GET.get('userId')

    filters = {'adType': {"$ne": "sold"}}
    if ad_type:
        filters['adType'] = ad_type
    if type:
        filters['type'] = type
    if country:
        filters['address.country'] = country
    if city:
        filters['address.city'] = city
    if floor:
        filters['address.floor'] = int(floor)
    if room:
        filters['rooms'] = int(room)
    if user_id:
        filters['userId'] = user_id

    properties = list(collection.find(filters))
    response = {
        "adType": list(set(prop.get('adType') for prop in properties)),
        "type": list(set(prop.get('type') for prop in properties)),
        "country": list(set(prop.get('address', {}).get('country') for prop in properties if prop.get('address'))),
        "city": list(set(prop.get('address', {}).get('city') for prop in properties if prop.get('address'))),
        "floor": list(set(prop.get('address', {}).get('floor') for prop in properties if prop.get('address'))),
        "rooms": list(set(prop.get('rooms') for prop in properties)),
    }

    return JsonResponse(response)
