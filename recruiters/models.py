
from users.models import  CustomUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone

 
class RecruiterProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    recruiter_name=models.CharField(_("name"),default='xyz', max_length=50)
    company_name=models.CharField(_("Your company name"), max_length=50)
    contact_email=models.EmailField(_("Company Email"), max_length=254)
    contact_phone=models.CharField(_("Phone number"), max_length=50,blank=True,null=True)
    location=models.CharField(_("Location "),max_length=50,default='New Dehli')
    bio=models.TextField(_("Write your bio here!!!!!!!"),max_length=50,blank=True)
    
    def __str__(self):
        return f"{self.user.email} have {self.company_name} with {self.contact_email}"

class Job(models.Model):
    recruiter = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'recruiter'}
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(
        max_length=50,
        choices=[
            ('full-time', 'Full-time'),
            ('part-time', 'Part-time'),
            ('internship', 'Internship')
        ]
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    requirements = models.TextField(help_text="List of job requirements")
    experience_required = models.CharField(
        max_length=100,
        help_text="Required experience level"
    )
    specifications = models.TextField(
        null=True,
        blank=True,
        help_text="Any other specific requirements"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


