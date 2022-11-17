from django.urls import path

from .views import *

urlpatterns = [
    # path('address/create', create_address),
    path('address/get_cities', get_cities),
    path('address/get_districts', get_districts),
    path('address/get_wards', get_wards),
]
