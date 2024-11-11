from operator import itemgetter

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
