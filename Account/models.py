from users.models import CustomUser 
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from .models import CustomUser

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
    USER_TYPE_CHOICES=CustomUser.USER_TYPE_CHOICES

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # user_type = models.CharField(
    #     max_length=10,
    #     choices=USER_TYPE_CHOICES,
    #     default='candidate',  # Default to 'candidate'
    # )
    first_name=models.CharField(_("First Name"),default='xyz', max_length=50)
    last_name=models.CharField(_("Last Name"),default='xyz', max_length=50)
    education= models.CharField(_("Add your education criteria"), max_length=50,choices=EDUCATION_CHOICES,default='masters')
    experience=models.CharField(_("Your work wxperience level"), max_length=50,choices=EXPERIENCE_CHOICES, default='0-1')
    has_resume=models.BooleanField(_("Do you have resume"),default=True,max_length=5)
    resume=models.FileField(_("Upload your resume here"), upload_to='profiles/', max_length=100,blank=True)
    gender=models.CharField(_("Select your gender "), max_length=50,choices=gender_chioce,default="")
    bio=models.TextField(_("Write your bio here!"),blank=True)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name} with the email {self.user.email}' 
class RecruiterProfile(models.Model):
    USER_TYPE_CHOICES=CustomUser.USER_TYPE_CHOICES
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # user_type = models.CharField(
    #     max_length=10,
    #     choices=USER_TYPE_CHOICES,
    #     default='recruiter',  # Default to 'candidate'
    # )
     
    company_name=models.CharField(_("Your company name"), max_length=50)
    company_logo=models.ImageField(_("Company Image"), upload_to='proImage',blank=True,null=True)
    contact_phone=models.CharField(_("Phone number"), max_length=50,blank=True,null=True)
    location=models.CharField(_("Location "),max_length=50,default='New Dehli')
    bio=models.TextField(_("Write your bio here!!!!!!!"),max_length=50,blank=True)
    
    def __str__(self):
        return f"{self.user.email} have {self.company_name} "