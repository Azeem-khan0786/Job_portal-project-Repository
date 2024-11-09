from django.contrib import admin
from django.urls import path
from jsonApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('importdata/', import_data,name='importdata'),
]