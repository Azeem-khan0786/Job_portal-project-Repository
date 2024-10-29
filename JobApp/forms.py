from django import forms
from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser
from JobApp.models import Job ,Applicant ,BookmarkJob


#create form for create_job 
class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        exclude=['recruiter']

class JobApplyForm(forms.ModelForm):
    
    class Meta:
        model = Applicant
        fields = ("job",)

class BookmarkJobForm(forms.ModelForm):
    
    class Meta:
        model = BookmarkJob
        fields = ("job",)


    
        

    

   
