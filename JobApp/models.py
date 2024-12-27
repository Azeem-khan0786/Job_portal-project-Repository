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


# class for Technical skill
class Skill(models.Model):
    skill_name=models.CharField(_("skill"), max_length=200)
    def __str__(self):
             return self.skill_name

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
    skills =models.ManyToManyField("Skill", related_name='technical_skill',blank=True)
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

    
class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

# model to create resume
class Resume(models.Model):
    # Choices for title
    TITLE_CHOICES = [
        ("Software Developer", "Software Developer"),
        ("Data Analyst", "Data Analyst"),
        ("Project Manager", "Project Manager"),
        ("UI/UX Designer", "UI/UX Designer"),
        ("Other", "Other"),
    ]

    # Choices for education
    EDUCATION_CHOICES = [
        ("High School", "High School"),
        ("Associate Degree", "Associate Degree"),
        ("Bachelor's Degree", "Bachelor's Degree"),
        ("Master's Degree", "Master's Degree"),
        ("Ph.D.", "Ph.D."),
    ]

    # Choices for experience level
    EXPERIENCE_CHOICES = [
        ("Entry Level", "Entry Level (0-2 years)"),
        ("Mid Level", "Mid Level (2-5 years)"),
        ("Senior Level", "Senior Level (5+ years)"),
    ]
    SKILLS_CHOICES = [
    ("Python", "Python"),
    ("Django", "Django"),
    ("JavaScript", "JavaScript"),
    ("React", "React"),
    ("HTML", "HTML"),
    ("CSS", "CSS"),
    ("SQL", "SQL"),
    ("Java", "Java"),
    ("C++", "C++"),
    ("Other", "Other"),
   ]

    username = models.OneToOneField(
        CustomUser,  # Use your custom user model here if applicable
        on_delete=models.CASCADE,
        related_name="resume"
    )
    title = models.CharField(
        max_length=50,
        choices=TITLE_CHOICES,
        default="Other",
        help_text="Title of the resume. Choose the most appropriate role."
    )
    objective = models.TextField(
        max_length=1000,
        help_text="A short paragraph about the candidate's career objectives and aspirations."
    )
    skills = models.ManyToManyField('Skill',
    max_length=255,
    
    default="Java",
    help_text="Select a key skill. Add multiple skills by creating separate entries.")
    experience = models.CharField(
        max_length=50,
        choices=EXPERIENCE_CHOICES,
        default="Entry Level",
        help_text="Select the experience level of the candidate."
    )
    education = models.CharField(
        max_length=50,
        choices=EDUCATION_CHOICES,
        default="Bachelor's Degree",
        help_text="Select the highest level of education attained."
    )
    certifications = models.TextField(
        blank=True,
        help_text="Details of certifications or training. Use JSON or plain text for multiple entries."
    )
    achievements = models.TextField(
        blank=True,
        help_text="List of notable achievements or awards. Use JSON or plain text."
    )
    projects = models.TextField(
        blank=True,
        help_text="Summary of significant projects with details. Use JSON or plain text."
    )
    resume_file = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True,
        help_text="Upload a PDF or document version of the resume."
    )
    linkedin_profile = models.URLField(
        blank=True,
        help_text="URL to the candidate's LinkedIn profile."
    )
    portfolio_website = models.URLField(
        blank=True,
        help_text="URL to the candidate's portfolio or personal website."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}'s Resume"
    

# Comment Model 
class CommentModel(models.Model):
    user=models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    job= models.ForeignKey('Job', related_name='job', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at=models.DateTimeField( auto_now_add=True)

    
        
    
