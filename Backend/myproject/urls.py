from django.contrib import admin
from django.urls import path

from myapp.views import (get_properties_by_user,
                         get_property,
                         get_filter_parameter,
                         get_properties,
                         create_property_view,
                         delete_property_by_id,
                         sold_property_by_id,
                         update_property,
                         get_dashboard,
                         get_revenue_for_year,
                         get_last_properties)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dashboard', get_dashboard),
    path('api/dashboard/revenue/<int:year>', get_revenue_for_year),
    path('api/property/latest/<int:number>', get_last_properties),
    path('api/filter', get_filter_parameter),
    path('api/property', get_properties),
    path('api/property/<str:property_id>', get_property),
    path('api/property/user/<str:user_id>', get_properties_by_user),
    path('api/properties', create_property_view),
    path('api/property/delete/<str:property_id>', delete_property_by_id),
    path('api/property/sold/<str:property_id>', sold_property_by_id),
    path('api/property/update/<str:property_id>', update_property),
]
