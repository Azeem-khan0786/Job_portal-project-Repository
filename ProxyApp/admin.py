from django.contrib import admin
from .models import MainModel,ProxyModel
# Register your models here.
admin.site.register(MainModel)
admin.site.register(ProxyModel)