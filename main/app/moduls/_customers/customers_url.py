from django.urls import path

from . import customers_view

urlpatterns = [
    path('customers/', customers_view.customersList),
]
