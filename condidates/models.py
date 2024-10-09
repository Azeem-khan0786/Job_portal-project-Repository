
from users.models import  CustomUser
from django.utils.translation import gettext_lazy as _
from django.db import models

gender_chioce=(( "m","male"
    
),('f','female'),('oth','Others'),)
status_choices=(('apl','applied'),('intw','intervew'),('hrd','hired'),('rjct','rejected'),)
   # Predefined choices for education
EDUCATION_CHOICES = [
        ('high_school', 'High School'),
        ('bachelors', 'Bachelor\'s Degree'),
        ('masters', 'Master\'s Degree'),
        ('phd', 'PhD'),
        ('other', 'Other'),
    ]
    
    # Predefined choices for experience level
EXPERIENCE_CHOICES = [
        ('0-1', '0-1 Years'),
        ('2-3', '2-3 Years'),
        ('4-5', '4-5 Years'),
        ('6-10', '6-10 Years'),
        ('10+', 'More than 10 Years'),
    ]
 
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name=models.CharField(_("first_name"),default='xyz', max_length=50)
    last_name=models.CharField(_("last_name"),default='xyz', max_length=50)
    cond_email=models.EmailField(_("Email-address"), max_length=254,unique=True,default="")
    skill= models.CharField(_("Add your skills"), max_length=50,choices=EDUCATION_CHOICES,default='masters')
    experience=models.CharField(_("your work wxperience level"), max_length=50,choices=EXPERIENCE_CHOICES, default='0-1')
    has_resume=models.BooleanField(_("has_resume"),default=True,max_length=5)
    resume=models.FileField(_("Resume"), upload_to='profiles/', max_length=100,blank=True)
    gender=models.CharField(_("Choice "), max_length=50,choices=gender_chioce,default="")
    bio=models.TextField(_("Write your bio here!!!!!!!"),blank=True)
    

    def __str__(self):
        return self.first_name

   
 
class JobApplication(models.Model):
    condidate=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_id=models.CharField( max_length=50)
    job_title=models.CharField(_("job Title"), max_length=50)
    status=models.CharField(max_length=50, choices=status_choices,default='apl')
    applied_on=models.DateTimeField(_("Applied DateTime"), auto_now_add=True)  
    
    def __str__(self):
        return f"{self.condidate.email} applied for {self.job_id} at {self.applied_on}"
    
   

   