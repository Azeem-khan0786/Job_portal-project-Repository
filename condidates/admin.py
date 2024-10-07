from django.contrib import admin
from condidates.models import CondidateProfile
# from .models import CondidateProfile
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(CondidateProfile)

admin.site.register(User)



# @admin.register(CondidateProfile)
class CondidateProfileAdmin(admin.ModelAdmin):
    list_display=['cond_email','is_condidate','status','date_applied']
admin.site.register(CondidateProfile,CondidateProfileAdmin)    
    

     