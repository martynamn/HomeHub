import email

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods

from myapp.services import dashboard
from myapp.services import filter
from myapp.services import property


@require_GET
def get_dashboard(request):
    user_id = request.GET.get('userId')
    if not user_id:
        return JsonResponse({'error': 'userId is required'}, status=401)
    return dashboard.get_dashboard(user_id)


@require_GET
def get_revenue_for_year(request, year: int):
    user_id = request.GET.get('userId')
    if not user_id:
        return JsonResponse({'error': 'userId is required'}, status=401)
    return dashboard.get_revenue_for_year(year, user_id)


@require_GET
def get_last_properties(request, number: int):
    user_id = request.GET.get('userId')
    if not user_id:
        return JsonResponse({'error': 'userId is required'}, status=401)
    return property.get_last_properties(number, user_id)


@require_GET
def get_properties_by_user(request, user_id: str):
    response = property.get_properties_by_user(user_id)
    if response is None:
        return JsonResponse({'error': 'No properties found for this user'}, status=404)
    return response


@csrf_exempt
@require_POST
def create_property_view(request):
    metadata = request.POST.get('metadata')
    files = request.FILES.getlist('files')

    if not metadata:
        return JsonResponse({'error': 'Metadata is required.'}, status=400)
    if not files:
        return JsonResponse({'error': 'Image files are required.'}, status=400)

    response = property.create_property(metadata, files)
    if 'error' in response:
        return JsonResponse(response, status=400)
    return JsonResponse(response, status=201)


@require_http_methods(['DELETE'])
@csrf_exempt
def delete_property_by_id(request, property_id):
    response = property.delete_property_by_id(property_id)
    if 'error' in response:
        return JsonResponse(response, status=404)
    return JsonResponse(response, status=200)


@require_http_methods(['PUT'])
@csrf_exempt
def sold_property_by_id(request, property_id):
    response = property.sold_property_by_id(property_id)
    if 'error' in response:
        return JsonResponse(response, status=404)
    return JsonResponse(response, status=200)


@require_http_methods(['PUT'])
@csrf_exempt
def update_property(request, property_id: str):
    try:
        message = email.message_from_bytes(request.body)
        message_lines = message.as_string().split('\n')
        metadata = None
        for i in range(len(message_lines) - 1):
            if 'metadata' in message_lines[i]:
                metadata = message_lines[i + 2]
            if 'files' in message_lines[i]:
                files = message_lines[i]

        if not metadata:
            return JsonResponse({'error': 'Metadata is required.'}, status=400)
        if not files:
            return JsonResponse({'error': 'Image files are required.'}, status=400)

        response = property.update_property_by_id(property_id, metadata, files)
        if 'error' in response:
            return JsonResponse(response, status=404)
        return JsonResponse(response, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@require_GET
def get_filter_parameter(request):
    return filter.get_filter_parameters(request)


@require_GET
def get_properties(request):
    return property.get_properties(request)


@require_GET
def get_property(request, property_id: str):
    if id is None:
        return JsonResponse({'error': 'The property id cannot be null'}, status=404)
    return property.get_property(property_id)
