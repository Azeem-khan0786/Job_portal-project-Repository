from django import forms
from condidates.models import CondidateProfile
from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser

class CondidateRegisteration(UserCreationForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email','password1','password2',]
        
    
