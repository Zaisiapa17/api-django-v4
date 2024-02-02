from django.db import models
from app.moduls._customers.customers_model import Customer
from app.moduls._products.products_model import Product


class OrderContainer(models.Model):
    class Meta:
        db_table = '_order_containers'
        unique_together = ('customer', 'product')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"OrderContainer {self.id} - Customer: {self.customer.customer_name}"