from django import forms
from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser
from JobApp.models import Job ,Applicant


#create form for create_job 
class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'

class JobApplyForm(forms.ModelForm):
    
    class Meta:
        model = Applicant
        fields = ("job",)

    
        

    

   
