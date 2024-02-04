from rest_framework import serializers

from . import customers_model
from app.moduls._customers_orders import customers_orders_model


class CustomerSerializer(serializers.ModelSerializer):
    total_orders = serializers.SerializerMethodField()

    class Meta:
        model = customers_model.Customer
        fields = ['id', 'customer_name', 'phone', 'email', 'password', 'total_orders']

    def get_total_orders(self, obj):
        return customers_orders_model.OrderContainer.objects.filter(customer=obj).count()


class ActCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = customers_model.Customer
        fields = ['id', 'customer_name', 'phone', 'email', 'password']