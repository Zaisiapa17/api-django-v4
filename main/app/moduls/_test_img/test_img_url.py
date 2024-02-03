from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import test_img_view

urlpatterns = [
    path('upload-img/', test_img_view.upload_file)
]
