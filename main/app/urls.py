from django.urls import path, include

urlpatterns = [ 
    path("", include("app.moduls._customers.customers_url")),
    path("", include("app.moduls._customers_orders.customers_orders_url")),
    path("", include("app.moduls._test_img.test_img_url")),
]