from django.contrib import admin
from django.contrib.auth.models import User
from .models import  UserProfile,JobApplication
# Register your models here.
admin.site.register(User)

admin.site.register(UserProfile)

admin.site.register(JobApplication)
    

     