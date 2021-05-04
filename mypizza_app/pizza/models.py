from typing import Sized
from django.db import models
from django.db.models.enums import Choices

# Create your models here.

TYPE_CHOICES=[('regular','REGULAR'),('square','SQUARE')]

class PizzaSize(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class PizzaToppings(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class Pizza(models.Model):
    type=models.CharField(choices=TYPE_CHOICES,max_length=100,blank=True,null=True)
    size=models.ForeignKey(PizzaSize,blank=True,null=True,on_delete=models.CASCADE)
    topping=models.ForeignKey(PizzaToppings,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.type+"-"+self.size+"-"+self.topping