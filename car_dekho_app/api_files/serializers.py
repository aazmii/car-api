from rest_framework import serializers

from car_dekho_app.models.cars import Cars
class CarSerializier (serializers.Serializer): 
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField(read_only = True)

    def create (self ,validatedData): 
        return Cars.objects.create(**validatedData)
    
    def update(self, instance,validatedData): 
        instance.name = validatedData.get('name', instance.name)
        instance.description = validatedData.get('description', instance.description)
        instance.active = validatedData.get('active', instance.active)
        instance.save()
        return instance
    
