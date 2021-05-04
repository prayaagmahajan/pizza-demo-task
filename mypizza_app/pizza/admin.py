from django.contrib import admin
from .models import Pizza,PizzaSize,PizzaToppings
# Register your models here.
admin.site.register(Pizza)
admin.site.register(PizzaSize)
admin.site.register(PizzaToppings)