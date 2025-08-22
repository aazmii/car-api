from rest_framework import serializers
class CarSerializier (serializers.Serializer): 
    id = serializers.IntegerField(read_only = True)
    carName = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField(read_only = True)