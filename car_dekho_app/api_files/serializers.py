from rest_framework import serializers

from car_dekho_app.models.cars import Cars
def alphanumeric (value): 
    if not str(value).isalnum():
        raise serializers.ValidationError('name should be alphanumeric')

class CarSerializier (serializers.Serializer): 
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField(read_only = True)
    chassisnumber = serializers.CharField(validators = [alphanumeric])
    price = serializers.DecimalField(max_digits = 9, decimal_places= 2)

    def create (self ,validated_data): 
        
        return Cars.objects.create(**validated_data)
    
    def update(self, instance,validated_data): 
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.chassisnumber = validated_data.get('chassisnumber', instance.chassisnumber)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    
    #FIELD LEVEL VALIDATION
    def validate_price(self, value): 
        if value <= 20000: 
            raise serializers.ValidationError("price should be greater than 20000")
        return value
    
    # OBJECT LEVEL VALIDATOR
    def validate(self,data): 
        if data['name'] == data['description']: 
            raise serializers.ValidationError('Name and description should not be same')
        return data #must return the data
        
    #CUSTOM VALIDATORS
    # -> SEE alphanumeric