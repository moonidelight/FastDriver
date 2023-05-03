from rest_framework import serializers

from .models import Car, Order, Category, Payment


class CarSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(required=False)
    model = serializers.CharField(required=False)
    img = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    transmission = serializers.CharField(required=False)
    volume = serializers.FloatField(required=False)
    fuelType = serializers.CharField(required=False)
    rentingPrice = serializers.FloatField(required=False)
    available = serializers.BooleanField(required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        # for field in validated_data:
        #     setattr(instance, field, validated_data[field])
        instance.available = validated_data.get('available', instance.available)
        instance.rentingPrice = validated_data.get('price', instance.rentingPrice)
        instance.save()
        return instance


class PaymentSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    id = serializers.IntegerField(read_only=True)
    card_number = serializers.CharField()
    activated_month = serializers.IntegerField()
    activated_year = serializers.IntegerField()
    cvv = serializers.IntegerField()

    def create(self, validated_data):
        card = Payment.objects.create(**validated_data)
        return card


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cars = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), many=True)

    class Meta:
        model = Order
        fields = ('id', 'cars', 'user', 'date_created')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
