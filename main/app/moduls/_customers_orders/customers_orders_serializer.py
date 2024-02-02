from rest_framework import serializers

from . import customers_orders_model

class ItemsCheckOutSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name', read_only=True)
    product_price = serializers.CharField(source='product.price', read_only=True)

    class Meta:
        model = customers_orders_model.OrderContainer
        fields = ['id', 'product_name', 'product_price', 'created_at', 'updated_at']