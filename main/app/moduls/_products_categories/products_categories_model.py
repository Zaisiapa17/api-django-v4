from django.db import models

class Category(models.Model):
    class Meta:
        db_table = '_categories'
    name = models.CharField(max_length=255)