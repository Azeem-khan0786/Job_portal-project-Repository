from django import forms
from recruiters.models import RecruiterProfile

class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model=RecruiterProfile
        fields="__all__"
    
