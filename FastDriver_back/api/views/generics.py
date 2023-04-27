from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.serializers import CarSerializer
from api.models import Car


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
