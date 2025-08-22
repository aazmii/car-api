# Create your views here.
from django.http import JsonResponse
from car_dekho_app.models.cars import Cars


def carList(request): 
    cars = Cars.objects.all()
    data = {
        'cars:': list(cars.values())
    }
    return JsonResponse(data)

def carDetail(request, id): 
    car = Cars.objects.get(id =id)
    data = {
        'name': car.carName,
        'description': car.description,
        'active': car.active,
    }
    return JsonResponse(data)