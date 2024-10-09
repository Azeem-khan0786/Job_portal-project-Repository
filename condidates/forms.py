from django import forms
from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser
from condidates.models import UserProfile

#  1. Condidates registration Form
class CondidateRegisteration(UserCreationForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email','password1','password2',]
        
        
# 2.  condidates profile form 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

    

   
