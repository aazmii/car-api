from django.urls import path

from car_dekho_app.views.car_view import car_detail, car_list 
 
urlpatterns = [
    path('cars/', car_list, name='car_list'),
    path ('<int:id>/', car_detail, name = 'car_detail'),
]