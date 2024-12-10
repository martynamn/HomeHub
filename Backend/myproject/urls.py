from django.contrib import admin
from django.urls import path

from myapp.views import get_property, get_dashboard, get_revenue_for_year, get_last_properties, get_filter_parameter, get_properties

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dashboard', get_dashboard),
    path('api/dashboard/revenue/<int:year>', get_revenue_for_year),
    path('api/property/latest/<int:number>', get_last_properties),
    path('api/filter', get_filter_parameter),
    path('api/property', get_properties),
    path('api/property/<str:property_id>', get_property),

]
