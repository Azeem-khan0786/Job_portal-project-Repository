
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models
# from users.models import CustomUser
gender_chioce=(( "m","male"
    
),('f','female'),('oth','Others'),)
# Create your models here.

class CondidateProfile(models.Model):
    #  username=models.OneToOneField(User, on_delete=models.CASCADE)
     firstname = models.CharField(max_length=100, default='Azeemkhan',null=True)
     lastname=models.CharField( max_length=50,default='khan')
     email_add = models.EmailField(_("Email Address"), max_length=254, help_text=_("Enter a valid email address."),default='xyxz@xyz.in',null=False)
     password = models.CharField(_("Password"), max_length=128,null=True) 
     is_employed=models.BooleanField(default=False)
     experience=models.CharField(_("Work Experience"), max_length=50,null=True,blank=True)
     image=models.ImageField(_("UsersImage"), upload_to="ImageArea", null=True, height_field=None, width_field=None, max_length=None)
     resume=models.FileField(_("Your Resume"), upload_to="Documents",null=True, max_length=100)
     phone_no = models.CharField(_("Phone Number"), max_length=15) 
     gender=models.CharField(_("Gender"), max_length=3,choices=gender_chioce,blank=True,null=True)
     is_educated=models.BooleanField(default=True)
     
     def __str__(self):
            return f"{self.firstname} {self.lastname}"
     
