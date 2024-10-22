from django.shortcuts import render,HttpResponseRedirect ,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from JobApp.models import  Job
from JobApp.forms import  JobForm
from users.models import CustomUser

from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .permission import *



# from recruiters.models import Job
    
def job_view(request):
    jobs=Job.objects.all()
    # {{jobs.title}}
    return render(request, 'JobApp/jobPage.html', {'jobs':jobs})    
   
# specifice job list view for recruiter
@login_required(login_url=reverse_lazy('Account:signin'))      
@user_is_recruiter
def recruiter_job_view(request):
    if request.user.is_authenticated:
        recruiter_jobs=Job.objects.filter(recruiter=request.user)
        print(request.user)
        # {{recruiter_jobs}}
        return render(request, 'JobApp/recruiterJobPage.html', {'recruiter_jobs':recruiter_jobs})
    else:
        return redirect('Account:signin')


def custom_csrf_failure(request, reason=""):
    return render(request, "csrf_failure.html", {"reason": reason})   

# method to create job by recruiter        
@login_required(login_url=reverse_lazy('Account:signin'))      
@user_is_recruiter
def create_job(request):
     ''' 
     Create Job  if @user_is_recruiter  
    
     '''

     user=get_object_or_404(CustomUser,id=request.user.id)
     if request.method=='POST':
        form =JobForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=user
            instance.save()
            return redirect('JobApp:job_view')
     else:
         form=JobForm()    
     context={'form':form}
     template_name='JobApp/create_job.html'
     return render(request, template_name, context)
    
def job_details(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        data = {
            'title': job.title,
            'description': job.description,
            'location': job.location,
            'job_type': job.get_job_type_display(),
            'salary': job.salary if job.salary else 'Not specified',
            'experience_required': job.experience_required,
            'education': job.get_education_display(),
            'language': job.language,
            'schedule': job.schedule,
            'work_mode': job.get_work_mode_display(),
            'requirements': job.requirements,
            'specifications': job.specifications if job.specifications else '',
            'Vacancy': job.Vacancy if job.Vacancy else 'Not specified'
        }
        return JsonResponse(data)
    except Job.DoesNotExist:
        return JsonResponse({'error': 'Job not found'}, status=404)         

def single_job_view(request, id):
    """
    Provide the ability to view job details
    """
     
    single_job = get_object_or_404(Job, id=id)
    company = single_job.recruiter.recruiterprofile.company_name
    print('company_name',company)    
    context = {
        'single_job': single_job,
        'company': company,

        

    }
    
    return render(request, 'JobApp/job-single.html', context)        