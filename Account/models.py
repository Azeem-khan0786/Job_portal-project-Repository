from users.models import CustomUser 
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone

# Create your models here.
gender_chioce=(( "m","male"
    
),('f','female'),('oth','Others'),)

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
 
class CandidateProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name=models.CharField(_("first_name"),default='xyz', max_length=50)
    last_name=models.CharField(_("last_name"),default='xyz', max_length=50)
    cond_email=models.EmailField(_("Email-address"), max_length=254,unique=True,default="")
    education= models.CharField(_("Add your education"), max_length=50,choices=EDUCATION_CHOICES,default='masters')
    # skills =models.ManyToManyField("Skill", related_name='technical_skill',blank=True)
    experience=models.CharField(_("your work wxperience level"), max_length=50,choices=EXPERIENCE_CHOICES, default='0-1')
    has_resume=models.BooleanField(_("has_resume"),default=True,max_length=5)
    resume=models.FileField(_("Resume"), upload_to='profiles/', max_length=100,blank=True)
    gender=models.CharField(_("Choice "), max_length=50,choices=gender_chioce,default="")
    bio=models.TextField(_("Write your bio here!!!!!!!"),blank=True)
    

    def __str__(self):
        return self.first_name
class RecruiterProfile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    recruiter_name=models.CharField(_("name"),default='xyz', max_length=50)
    company_name=models.CharField(_("Your company name"), max_length=50)
    company_logo=models.ImageField(_("Image  Company"), upload_to='proImage',blank=True,null=True)
    contact_email=models.EmailField(_("Company Email"), max_length=254)
    contact_phone=models.CharField(_("Phone number"), max_length=50,blank=True,null=True)
    location=models.CharField(_("Location "),max_length=50,default='New Dehli')
    bio=models.TextField(_("Write your bio here!!!!!!!"),max_length=50,blank=True)
    
    def __str__(self):
        return f"{self.user.email} have {self.company_name} with {self.contact_email}"