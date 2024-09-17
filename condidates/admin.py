from django.contrib import admin
from condidates.models import CondidateProfile
class CondidateProfileAdmin(admin.ModelAdmin):
    list_display=('username','first_name','is_employed','is_educated',)
admin.site.register(CondidateProfile,CondidateProfileAdmin)  

