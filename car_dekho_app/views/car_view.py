# Create your views here.
from django.http import JsonResponse
from car_dekho_app.api_files.serializers import CarSerializier
from car_dekho_app.models.cars import Cars
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
@api_view(['GET', 'POST'])
def car_list(request): 
    if request.method == 'GET':
        car = Cars.objects.all()
        serializer = CarSerializier(car, many=True)
        return Response(serializer.data)
    if request.method == 'POST': 
        serializer = CarSerializier(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else : 
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request,id):
    if request.method == 'GET' :
        try: 
            car = Cars.objects.get(id =id)
        except: 
            return Response({'error': 'Car not found'}, status = status.HTTP_404_NOT_FOUND)
        serializer = CarSerializier(car)
        return Response(serializer.data)
    if(request.method =='PUT'): 

        car = Cars.objects.get(id = id)
        serializer = CarSerializier(car,data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else : 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    if request.method =='DELETE': 
        car = Cars.objects.get(id= id)
        car.deelte()
        return Response(status = status.HTTP_204_NO_CONTENT)