
from users.models import  CustomUser
from django.utils.translation import gettext_lazy as _
from django.db import models

# from users.models import CustomUser
gender_chioce=(( "m","male"
    
),('f','female'),('oth','Others'),)
status=(('apl','applied'),('intw','intervew'),('hrd','hired'),('rjct','rejected'),)
# Create your models here.

class CondidateProfile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    cond_email=models.EmailField(_("Email-address"), max_length=254,unique=True,default="")
    cond_password=models.CharField(_("Condidate password"), max_length=50,)
    is_condidate=models.BooleanField(_("is-condidate"), max_length=50,default=True)
    has_resume=models.BooleanField(_("has_resume"),default=True,max_length=5)
    date_applied=models.DateTimeField(_("Date Applied"),  auto_now_add=True)
    resume=models.FileField(_("Resume"), upload_to='resume/', max_length=100,blank=True)
    gender=models.CharField(_("Choice "), max_length=50,choices=gender_chioce,default="")
    status=models.CharField(_("Status"), max_length=50,choices=status,default='apl')
   
    About= models.TextField()
    def __str__(self):
        return f"{self.user} {self.cond_email}"

      