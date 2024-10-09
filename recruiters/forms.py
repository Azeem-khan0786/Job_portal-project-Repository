from django import forms
from recuiters.models import RecruiterProfile

class RecruiterProfileForm(forms.Form):
    class Meta:
        model=RecruiterProfile
        fields="__all__"
    
