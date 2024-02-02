from django.urls import path

from . import customers_orders_view

urlpatterns = [
    path('check-out/<int:pk>/', customers_orders_view.orderList),
    
]
