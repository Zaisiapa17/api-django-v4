from rest_framework import serializers

from . import customers_model


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = customers_model.Customer
        fields = ['id', 'customer_name', 'phone', 'email']