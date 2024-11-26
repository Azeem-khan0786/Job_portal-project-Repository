from django.contrib import admin
from django.contrib.auth.models import User
from JobApp.models import  JobApplication ,Job,Applicant ,BookmarkJob,Contact,Skill


# Register your models here.
admin.site.register(User)

admin.site.register(JobApplication)
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Applicant)
admin.site.register(BookmarkJob)
admin.site.register(Contact)


    

     