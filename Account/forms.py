from django import forms
from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser
from Account.models import CandidateProfile,RecruiterProfile
from django.forms import ModelForm, TextInput, EmailInput
from django.db import transaction

# from .choices import GENDER_CHOICES
from Account.models import gender_chioce,EDUCATION_CHOICES,EXPERIENCE_CHOICES # import choices form models.py 

#  1. Candidates registration Form
# class CandidateRegisteration(UserCreationForm):
#     email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Email Address'
#     }))
#     phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Phone Number'
#     }))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'First Name'
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Last Name'
#     }))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Password'
#     }))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Confirm Password'
#     }))

#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']
        
        
# 2.  candidates profile form 
class CandidateProfileForm(UserCreationForm):  # Inherit from UserCreationForm
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, required=True)
    experience = forms.ChoiceField(choices=EXPERIENCE_CHOICES, required=True)
    has_resume = forms.BooleanField(required=False)
    resume = forms.FileField(required=False)
    gender = forms.ChoiceField(choices=gender_chioce, required=True)
    bio = forms.CharField(
        max_length=342,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control col-md-12',
                'rows': 4,
                'placeholder': 'Enter your bio here...',
            }
        ),
        label="Bio",
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']  # Include password fields from UserCreationForm

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'candidate'  # Set user type as candidate
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        if commit:
            user.save()
            candidate = CandidateProfile.objects.create(
                user=user,
                first_name=self.cleaned_data.get('first_name'),
                last_name=self.cleaned_data.get('last_name'),
                education=self.cleaned_data.get('education'),
                experience=self.cleaned_data.get('experience'),
                has_resume=self.cleaned_data.get('has_resume'),
                resume=self.cleaned_data.get('resume'),
                gender=self.cleaned_data.get('gender'),
                bio=self.cleaned_data.get('bio'),
            )
            candidate.save()
        return user
                
   
class RecruiterProfileForm(UserCreationForm):  # Inherit from UserCreationForm
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    company_name = forms.CharField(max_length=244, required=True)
    company_logo = forms.ImageField(required=False)
    contact_phone = forms.CharField(max_length=255, required=False)
    location = forms.CharField(max_length=232, required=False)
    bio = forms.CharField(
        max_length=342,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control col-md-12',
                'placeholder': 'Enter your bio here...',
                'style': 'width: 100%;',
            }
        ),
        label="Bio",
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']  # Using UserCreationForm's fields

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'recruiter'  # Assign recruiter role
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        if commit:
            user.save()
            recruiter = RecruiterProfile.objects.create(
                user=user,
                company_name=self.cleaned_data.get('company_name'),
                company_logo=self.cleaned_data.get('company_logo'),
                contact_phone=self.cleaned_data.get('contact_phone'),
                location=self.cleaned_data.get('location'),
                bio=self.cleaned_data.get('bio'),
            )
            recruiter.save()
        return user
    

   
