from users.models import CustomUser 
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone


status_choices=(('apl','applied'),('intw','intervew'),('hrd','hired'),('rjct','rejected'),)
gender_chioce=(( "m","male"
    
),('f','female'),)
WORK_MODE_CHOICES = (('REMOTE', 'Remote'),
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid'),)
language= (('eng','English Language'),
('fran',"Franch Language"),('urdu','Urdu Language'),)

education= (('high_school', 'High School'),
        ('bachelors', 'Bachelor\'s Degree'),
        ('masters', 'Master\'s Degree'),
        ('phd', 'PhD'),
        ('other', 'Other'),)
shift= (('morning','Morning Shift'),
('evening','Evening Shift'),)      



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
    education=models.CharField(_("Education"), max_length=50,choices=education, default='masters')
    language=models.CharField(_("Languages"), max_length=50,choices=language,default='eng')
    schedule=models.CharField(_("Shift and schedule"), max_length=50,choices=shift,default='morning')
    work_mode = models.CharField(
        max_length=10, 
        choices=WORK_MODE_CHOICES, 
        default='Onsite',  # Default to 'Onsite'
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    Vacancy = models.CharField(max_length=10, null=True)
    passedout = models.CharField(max_length=30 ,default='2023-2024')
    timestamp = models.DateTimeField(auto_now=True)
    end_date = models.DateField(max_length=20, null=True,default='None')
    gender = models.CharField(max_length=30,choices=gender_chioce ,blank=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    candidate=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_id=models.CharField( max_length=50)
    job_title=models.CharField(_("job Title"), max_length=50)
    status=models.CharField(max_length=50, choices=status_choices,default='apl')
    applied_on=models.DateTimeField(_("Applied DateTime"), auto_now_add=True)  
    
    def __str__(self):
        return f"{self.candidate.email} applied for {self.job_id} at {self.applied_on}"
    
class Applicant(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now=False)  

    def __str__(self):
        return f"{self.job.title}  {self.user}"

class BookmarkJob(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now=False)

    class Meta:
        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")

    
    def __str__(self):
       return f"Bookmark by {self.user.email} for {self.job.title}"

    

    

   