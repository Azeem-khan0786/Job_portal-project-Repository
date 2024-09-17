from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    username=None  #Removed the username field*/
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
    
    def __str__(self):
        return self.email
    
    
    
