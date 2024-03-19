from django.urls import path 
from .views import * 

urlpatterns = [
    path('add-category/', add_category, name='add-category'), 
    path('update-category/<int:pk>/', update_category, name='update-category'), 
    path('add-room/', add_room, name='add-room'),
    path('update-room/<int:pk>/', update_room, name='update-room'), 
    path('book-room/<int:pk>/', book_room, name='book-room'), 
    path('update-booked-room/<int:pk>/', update_booked_room, name='update-booked-room'), 
    path('all-booked-rooms/', all_booked_rooms, name='all-booked-rooms'), 
    path('all-available-rooms/', all_available_rooms, name='all-available-rooms'), 
    path('check-out-guest/<int:pk>/', check_out_guest, name='check-out-guest')
]