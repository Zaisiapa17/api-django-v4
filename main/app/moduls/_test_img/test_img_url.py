from django.urls import path

from . import test_img_view

urlpatterns = [
    path('upload-img/', test_img_view),
]
