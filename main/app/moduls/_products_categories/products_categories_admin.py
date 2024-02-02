from django.contrib import admin

from . import products_categories_model

admin.site.register(products_categories_model.Category)