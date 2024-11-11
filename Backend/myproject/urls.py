from django.contrib import admin
from django.urls import path

from myapp.views import get_dashboard, get_revenue_for_year
from myapp.views import get_last_properties

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dashboard', get_dashboard),
    path('api/dashboard/revenue/<int:year>', get_revenue_for_year),
    path('api/property/latest/<int:number>', get_last_properties),

]
