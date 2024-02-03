from django.urls import path

from . import test_img_view

urlpatterns = [
    path('url/', test_img_view),
]
