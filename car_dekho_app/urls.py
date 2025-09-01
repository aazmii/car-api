from django.urls import path

from car_dekho_app.views.car_view import car_detail, car_list
from car_dekho_app.views.showroom_view import ShowroomView 
 
urlpatterns = [
    path('cars/', car_list, name='car_list'),
    path ('<int:id>/', car_detail, name = 'car_detail'),
    path('showrooms/',  ShowroomView.as_view(), name='showroom_list'),
]