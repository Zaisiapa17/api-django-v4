from django.urls import path, include

urlpatterns = [ 
    path("", include("app.moduls._customers.customers_url")),
]