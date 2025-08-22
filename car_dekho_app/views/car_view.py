# Create your views here.
from django.http import JsonResponse
from car_dekho_app.api_files.serializers import CarSerializier
from car_dekho_app.models.cars import Cars
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def carList(request): 
    car = Cars.objects.all()
    serializer = CarSerializier(car, many=True)
    return Response(serializer.data)
@api_view()
def carDetail(request,id): 
    car = Cars.objects.get(id =id)
    serializer = CarSerializier(car)
    return Response(serializer.data)