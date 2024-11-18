from django.contrib import admin
from django.urls import path

from myapp.views import get_dashboard, get_revenue_for_year
from myapp.views import get_last_properties
from myapp.views import get_properties_by_user
from myapp.views import get_property_by_id
from myapp.views import create_property_view
from myapp.views import delete_property_by_id
from myapp.views import sold_property_by_id
from myapp.views import update_property
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dashboard', get_dashboard),
    path('api/dashboard/revenue/<int:year>', get_revenue_for_year),
    path('api/property/latest/<int:number>', get_last_properties),
    path('api/property/user/<str:user_id>', get_properties_by_user),
    path('api/property/<str:property_id>', get_property_by_id),
    path('api/property', create_property_view),
    path('api/property/delete/<str:property_id>', delete_property_by_id),
    path('api/property/sold/<str:property_id>', sold_property_by_id),
    path('api/property/update/<str:property_id>', update_property),
]



