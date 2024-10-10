from django import forms
from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser
from candidates.models import CandidateProfile

#  1. Candidates registration Form
class CandidateRegisteration(UserCreationForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email','password1','password2',]
        
        
# 2.  candidates profile form 
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        exclude = ['user']

    

   
