from django import forms
form condidates.model import CondidateProfile
from django.contrib.auth.forms import UserCreationForm

class CondidateRegisteration(UserCreationForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=CondidateProfile
        fields=['username','email','password1','password2',]
        
    
