from django.contrib import admin
from django.contrib.auth.models import User
from Account.models import  CandidateProfile,RecruiterProfile

# Register your models here.

 


# Register your models here.
admin.site.register(User)
admin.site.register(CandidateProfile)
admin.site.register(RecruiterProfile)
