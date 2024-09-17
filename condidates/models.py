
from django.contrib.auth.models import User
from django.db import models
# from users.models import CustomUser

# Create your models here.

class CondidateProfile(models.Model):
     first_name=models.OneToOneField(User, on_delete=models.CASCADE),
     is_employed=models.BooleanField(default=False),
     is_educated=models.BooleanField(default=True),
     
     def __str__(self):
         return self.first_name
     
