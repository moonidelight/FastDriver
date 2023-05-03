from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.serializers import CarSerializer, PaymentSerializer
from api.models import Car, Payment


class CarList(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)


class CarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PaymentAPIView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)
