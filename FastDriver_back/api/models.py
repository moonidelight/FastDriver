import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from rest_framework import serializers

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    img = models.TextField()
    city = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    volume = models.FloatField()
    fuelType = models.CharField(max_length=100)
    rentingPrice = models.FloatField()
    available = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cars', default=1, null=True)


class Order(models.Model):
    cars = models.ManyToManyField(Car)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.id}'
