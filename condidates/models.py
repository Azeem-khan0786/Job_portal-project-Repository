
from users.models import  CustomUser
from django.utils.translation import gettext_lazy as _
from django.db import models

gender_chioce=(( "m","male"
    
),('f','female'),('oth','Others'),)
status=(('apl','applied'),('intw','intervew'),('hrd','hired'),('rjct','rejected'),)
 
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name=models.CharField(_("first_name"),default='xyz', max_length=50)
    last_name=models.CharField(_("last_name"),default='xyz', max_length=50)
    cond_email=models.EmailField(_("Email-address"), max_length=254,unique=True,default="")
    cond_password=models.CharField(_("Condidate password"), max_length=50,default=True)
    is_condidate=models.BooleanField(_("is-condidate"), max_length=50,default=True)
    has_resume=models.BooleanField(_("has_resume"),default=True,max_length=5)
    date_applied=models.DateTimeField(_("Date Applied"),  auto_now_add=True)
    resume=models.FileField(_("Resume"), upload_to='profiles/', max_length=100,blank=True)
    gender=models.CharField(_("Choice "), max_length=50,choices=gender_chioce,default="")
    status=models.CharField(_("Status"), max_length=50,choices=status,default='apl')
    

    class Meta:
        verbose_name = _("UserProfile")
        verbose_name_plural = _("UserProfiles")

    def __str__(self):
        return self.first_name

   
 

    
    

   

   