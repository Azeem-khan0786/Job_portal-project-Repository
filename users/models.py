from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username=None  #Removed the username field*/
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("join date"), default=timezone.now) 
    USER_TYPE_CHOICES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
    )
    user_type = models.CharField(max_length=10,choices=USER_TYPE_CHOICES)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
    
    def __str__(self):
        return  f'{self.email} customUser'

# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, created, **kwargs):
#     from Account.models import CandidateProfile ,RecruiterProfile
    
#     if created:
#         if instance.user_type == 'candidate':
#             CandidateProfile.objects.create(user=instance)
#             print(f'Created CandidateProfile for {instance.email}')
#         elif instance.user_type == 'recruiter':
#             RecruiterProfile.objects.create(user=instance)
#             print(f'Created RecruiterProfile for {instance.email}')
#     else:
#         print(f'Profile save triggered for {instance.email}')
# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
#     if instance.user_type == 'candidate':
#         instance.candidateprofile.save()
#     elif instance.user_type == 'recruiter':
#         instance.recruiterprofile.save() 


# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, created, **kwargs):
#     # Ensure profiles are created only when a new CustomUser instance is created
#     if created:
#         if instance.user_type == 'candidate':
#             # Create the CandidateProfile if it's a new candidate user
#             CandidateProfile.objects.create(user=instance)
#             print(f'Created CandidateProfile for {instance.email}')
#         elif instance.user_type == 'recruiter':
#             # Create the RecruiterProfile if it's a new recruiter user
#             RecruiterProfile.objects.create(user=instance)
#             print(f'Created RecruiterProfile for {instance.email}')
#     else:
#         print(f'Profile save triggered for {instance.email}')


# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
    # Save the profile if it exists
    # if instance.user_type == 'candidate' and hasattr(instance, 'candidateprofile'):
    #     instance.candidateprofile.save()
    # elif instance.user_type == 'recruiter' and hasattr(instance, 'recruiterprofile'):
    #     instance.recruiterprofile.save()

