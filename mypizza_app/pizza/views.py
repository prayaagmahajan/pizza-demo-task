from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Pizza,PizzaSize,PizzaToppings
from .serializers import PizzaSerializer,PizzaSizeSerializer,PizzaToppingsSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

    
class PizzaViewset(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['size', 'topping']

class PizzaSizeViewset(viewsets.ModelViewSet):
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer

class PizzaToppingsViewset(viewsets.ModelViewSet):
    queryset = PizzaToppings.objects.all()
    serializer_class = PizzaToppingsSerializer
