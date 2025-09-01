from decimal import Decimal
from rest_framework import serializers

from car_dekho_app.models.cars import Cars
from car_dekho_app.models.showroom import Showrooms

class ShowroomSerializer (serializers.ModelSerializer): 
    class Meta: 
        model = Showrooms
        fields = ['id','name','location','website']




def alphanumeric (value): 
    if not str(value).isalnum():
        raise serializers.ValidationError('name should be alphanumeric')

class CarSerializier (serializers.ModelSerializer): 
    discounted_price = serializers.SerializerMethodField()
    class Meta: 
        model = Cars

        #adds all fields of the model,/
        fields = '__all__' 
        # fields= ['id','name','description','active','chassisnumber','price']
        # exclude = ['active'] 
        
        #fields that cannot be changed
        read_only_fields = ['id','active'] 
        
        #custom validators
        extra_kwargs = {
            'chassisnumber': {'validators': [alphanumeric]}
        }

    def get_discounted_price(self, obj): 
        if obj.price: 
            return obj.price * Decimal(0.9)
        return None

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