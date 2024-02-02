from django.contrib import admin

from . import customers_model

admin.site.register(customers_model.Customer)