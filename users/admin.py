from django.contrib import admin
from users.models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display=('first_name','is_employed', 'is_educated',)
admin.site.register(CustomUser,CustomUserAdmin)
    
    
