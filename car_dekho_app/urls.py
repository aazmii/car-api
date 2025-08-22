from django.urls import path

from car_dekho_app.views.car_view import carDetail, carList 
 
urlpatterns = [
    path('cars/', carList, name='car_list'),
    path ('<int:id>/', carDetail, name = 'car_detail'),
]