from django.contrib import admin

from . import customers_orders_model

admin.site.register(customers_orders_model.OrderContainer)
