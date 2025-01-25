from django import forms
from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser
from Account.models import CandidateProfile,RecruiterProfile
from django.forms import ModelForm, TextInput, EmailInput
from django.db import transaction


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
   
class RecruiterProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    company_name = forms.CharField(max_length=244, required=True)
    company_logo = forms.ImageField(required=False)  # No `upload_to` here; it belongs to the model
    contact_phone = forms.CharField(max_length= 255,required=False)
    location = forms.CharField(max_length=232,required=False)
    bio = forms.CharField(max_length= 342, required=False)


    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name','password']
    # class Meta:
    #     model=RecruiterProfile
    #     fields="__all__"        
    
    @transaction.atomic
    def save(self):
        # Save the user as a recruiter
        user = super().save(commit=False)
        user.user_type = 'recruiter'
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name= self.cleaned_data.get('last_name')
        user.save()

        # Create the recruiter's profile
        recruiter = RecruiterProfile.objects.create(user=user)
        recruiter.company_name = self.cleaned_data.get('company_name')
        recruiter.company_logo = self.cleaned_data.get('company_logo')
        recruiter.contact_phone = self.cleaned_data.get('contact_phone')
        recruiter.address = self.cleaned_data.get('location')
        recruiter.bio = self.cleaned_data.get('bio')
        recruiter.save()

        return user
    

   
