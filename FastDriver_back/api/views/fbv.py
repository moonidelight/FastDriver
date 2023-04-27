import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from api import serializers
from api.models import Car, Category


@api_view(['GET'])
def car_list(request):
    permission_classes = (AllowAny,)
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = serializers.CarSerializer(cars, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def car_detail(request, id):
    permission_classes = (AllowAny,)
    try:
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        serializer = serializers.CarSerializer(car)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        permission_classes = (IsAuthenticated,)
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def category_detail(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist as e:
        return Response(str(e), status=status.HTTP_404_BAD_REQUEST)

    if request.method == 'GET':
        cars = category.cars.all()
        serializer = serializers.CarSerializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        permission_classes = (IsAuthenticated,)
        category.delete()
        return Response({'deleted': True})
