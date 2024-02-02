from django.db import models
from app.moduls._products_categories.products_categories_model import Category

class Product(models.Model):
    class Meta:
        db_table = '_products'
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name