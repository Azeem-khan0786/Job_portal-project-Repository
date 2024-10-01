from django import forms
from condidates.models import CondidateProfile
from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser

class CondidateRegisteration(UserCreationForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=CustomUser
        fields='__all__'
        
    
