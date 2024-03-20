from django.urls import path 
from .views import *

urlpatterns = [
    path('add-hotel/', add_hotel, name='add-hotel'), 
    path('update-hotel/', update_hotel, name='update-hotel'), 
    path('hotel-details/', hotel_details, name='hotel-details')
]