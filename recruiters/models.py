
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
    bio=models.TextField(_("Write your bio here!!!!!!!"),blank=True)
    
    def __str__(self):
        return f"{self.user.email} have {self.company_name} with {self.contact_email}"

class JobModel(models.Model):
    recruiter = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE, related_name='jobs')  # Link to the recruiter
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=[('FT', 'Full-Time'), ('PT', 'Part-Time'), ('CT', 'Contract')])
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    posted_at = models.DateTimeField(default=timezone.now)
    application_deadline = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title