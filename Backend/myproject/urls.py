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
                         get_last_properties, create_user_view, get_users, get_user, set_subscription, update_user,
                         delete_user)

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
    path('api/properties/delete/<str:property_id>', delete_property_by_id),
    path('api/properties/sold/<str:property_id>', sold_property_by_id),
    path('api/properties/update/<str:property_id>', update_property),
    path('api/user', get_users),
    path('api/user/<str:user_id>', get_user),
    path('api/users', create_user_view),
    path('api/users/update/<str:user_id>', update_user),
    path('api/users/delete/<str:user_id>', delete_user),
    path('api/users/subscription/<str:user_id>', set_subscription)
]
