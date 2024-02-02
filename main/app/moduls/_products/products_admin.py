from django.contrib import admin

from . import products_model

admin.site.register(products_model.Product)