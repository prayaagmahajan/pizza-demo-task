from rest_framework import serializers
from .models import Pizza,PizzaSize,PizzaToppings
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pizza
        fields = '__all__'
        
class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PizzaSize
        fields = '__all__'

class PizzaToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PizzaToppings
        fields = '__all__'