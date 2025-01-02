from django import forms
from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser
from Account.models import CandidateProfile,RecruiterProfile
from django.forms import ModelForm, TextInput, EmailInput


#  1. Candidates registration Form
class CandidateRegisteration(UserCreationForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address'
    }))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone Number'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']
        
        
# 2.  candidates profile form 
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        exclude = ['user']

        widgets={'first_name': TextInput(attrs={
                'class': "form-control",
                
                'placeholder': 'Name',
                }),
                'last_name': TextInput(attrs={
                'class': "form-control",
                
                'placeholder': 'Name',
                }),
                }
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     # Assign user_type to candidate
    #     instance.user.user_type = 'candidate'
    #     if commit:
    #         instance.user.save()
    #         instance.save()
    #     return instance   

class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model=RecruiterProfile
        fields="__all__"        

    

   
