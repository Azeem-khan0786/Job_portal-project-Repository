
from django.contrib.auth.models import User
from django.db import models
# from users.models import CustomUser

# Create your models here.

class CondidateProfile(models.Model):
     username=models.OneToOneField(User, on_delete=models.CASCADE),
     first_name=models.CharField(max_length=234),
     is_employed=models.BooleanField(default=False),
     is_educated=models.BooleanField(default=True),
     address=models.TextField(max_length=333,blank=True),
     
     def __str__(self):
         return self.first_name +" " + self.first_name
     
