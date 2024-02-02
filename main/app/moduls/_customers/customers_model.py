from django.db import models

class Customer(models.Model):
    class Meta:
        db_table = '_customers'
    customer_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name