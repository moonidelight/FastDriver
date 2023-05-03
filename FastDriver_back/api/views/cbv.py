from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied

from api import serializers
from api.models import Order, Category


@method_decorator(csrf_exempt, name='dispatch')
class OrderList(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = serializers.OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = serializers.OrderSerializer()
        orders = Order.objects.filter(user=request.user)
        serializer = serializers.OrderSerializer(orders, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class OrderDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, id):
        try:
            order = Order.objects.get(pk=id)
            if order.user != self.request.user:
                raise PermissionDenied
            return order
        except Order.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_404_BAD_REQUEST)

    def get(self, request, id, format=None):
        instance = self.get_object(id)
        serializer = serializers.OrderSerializer(instance)
        return Response(serializer.data)
        # return Order.objects.filter(user=self.request.user)


@method_decorator(csrf_exempt, name='dispatch')
class Logout(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        # simply delete the session data for this user
        request.session.flush()
        return Response(status=204)
