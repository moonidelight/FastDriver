from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('logout/', views.logout),

    path('categories/', views.category_list),
    path('categories/<int:id>/cars/', views.category_detail),

    path('cars/', views.car_list),

    path('user/cars/', views.CarList.as_view()),
    path('user/cars/<int:pk>/', views.CarDetailAPIView.as_view()),

    path('user/order/', views.OrderList.as_view()),
    path('user/order/<int:id>/', views.OrderDetail.as_view()),

    path('user/order/payment/', views.PaymentAPIView.as_view()),
]
