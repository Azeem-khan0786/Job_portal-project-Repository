from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from django.contrib.auth.forms import UserCreationForm 
from users.models import  CustomUser
from JobApp.models import Job ,Applicant ,BookmarkJob ,Contact,Resume,CommentModel


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

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
# form to do_comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        fields='__all__'
    
        

# django form for post_resume
class ResumeForm(forms.ModelForm):
    
    class Meta:
        model = Resume
        # fields = '__all__'
        exclude=('username',)   
        
        widgets = {
            'skills': CheckboxSelectMultiple(),  # Render skills as checkboxes
         }

        def __init__(self, *args, **kwargs):
            super(ResumeForm, self).__init__(*args, **kwargs)

            # Add classes to form fields for better styling
            for field_name, field in self.fields.items():
                if isinstance(field.widget, forms.TextInput):
                    field.widget.attrs['class'] = 'form-control'
                elif isinstance(field.widget, forms.Textarea):
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['rows'] = 4
                elif isinstance(field.widget, forms.Select):
                    field.widget.attrs['class'] = 'form-control'
                elif isinstance(field.widget, forms.FileInput):
                    field.widget.attrs['class'] = 'form-control-file' 
    
        

    

   
