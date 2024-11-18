from django.http import JsonResponse
from django.views.decorators.http import require_GET

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
def get_filter_parameter(request):
    return filter.get_filter_parameters(request)

@require_GET
def get_properties(request):
    return property.get_properties(request)