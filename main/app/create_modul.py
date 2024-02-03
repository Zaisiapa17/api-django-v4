import os

file_names = ['_admin.py', '_controller.py', '_model.py', '_view.py', '_serializer.py', '_url.py']
modul_name = str(input("Enter module name: "))

os.makedirs(f'app/moduls/_{modul_name}', exist_ok=True)

dir_name = f'app/moduls/_{modul_name}/{modul_name}'

for i in file_names:
    with open(dir_name + i, 'w') as f:
        if i == '_admin.py':
            f.write(
f"""from django.contrib import admin

from . import {modul_name + file_names[2][:-3]}
admin.site.register({modul_name + file_names[2][:-3]})
""")
        elif i == '_controller.py':
            f.write(
f"""from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import {modul_name + file_names[2][:-3]}
from . import {modul_name + file_names[4][:-3]}
""")
        elif i == '_model.py':
            f.write(
"""from django.db import models
""")
        elif i == '_view.py':
            f.write(
f"""from rest_framework.decorators import api_view

from . import {modul_name + file_names[1][:-3]}
""")
        elif i == '_serializer.py':
            f.write(
f"""from rest_framework import serializers

from . import {modul_name + file_names[2][:-3]}
""")
        elif i == '_url.py':
            f.write(
f"""from django.urls import path

from . import {modul_name + file_names[3][:-3]}

urlpatterns = [
    path('url/', {modul_name + file_names[3][:-3]}),
]
""")
