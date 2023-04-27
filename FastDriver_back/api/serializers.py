from rest_framework import serializers

from .models import Car, Order, Category


class CarSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    fuel = serializers.CharField()
    volume = serializers.FloatField()
    kpp = serializers.CharField()
    price = serializers.FloatField()

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cars = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=True)

    class Meta:
        model = Order
        fields = ('id', 'cars', 'user')

    # def create(self, validated_data):
    #     cars_data = validated_data.pop('cars')
    #     order = Order.objects.create(**validated_data)
    #     for data in cars_data:
    #         car, created = Car.objects.get_or_create(**data)
    #         order.cars.add(car)
    #     return order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
