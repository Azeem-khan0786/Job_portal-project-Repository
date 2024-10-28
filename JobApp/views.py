from django.shortcuts import render,HttpResponseRedirect ,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from JobApp.models import  Job ,Applicant,BookmarkJob
from JobApp.forms import  JobForm , JobApplyForm ,BookmarkJobForm
from users.models import CustomUser

from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils import timezone
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
    com_logo=single_job.recruiter.recruiterprofile.company_logo
    print('company_name',company)    
    context = {
        'single_job': single_job,
        'company': company,
        'com_logo': com_logo,
    }
    return render(request, 'JobApp/job-single.html', context)        

# method for apply-job
@user_is_candidate
def apply_job_view(request, id):
    form = JobApplyForm(request.POST or None)
    user = get_object_or_404(CustomUser, id=request.user.id)
    job = get_object_or_404(Job, id=id)
    print(id)
    # Check if the applicant has already applied
    applicant_exists = Applicant.objects.filter(user=user, job=job).exists()

    if not applicant_exists:
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = user
                instance.job = job
                instance.timestamp = timezone.now()  # Set the timestamp
                instance.save()

                messages.success(request, 'You have successfully applied for this job!')
                return redirect(reverse('JobApp:single_job_view', kwargs={'id': id}))
        else:
            return redirect(reverse('JobApp:single_job_view', kwargs={'id': id}))
    
    # If already applied
    messages.warning(request, 'You have already applied for this job.')
    return redirect(reverse('JobApp:single_job_view', kwargs={'id': id}))


# method for job bookmark
@user_is_recruiter
def bookmark_view(request,id):
    form =BookmarkJobForm(request.POST or None)
    user=get_object_or_404(CustomUser,id=request.user.id)
    job=get_object_or_404(Job,id=id)
    applicant=BookmarkJob.objects.filter(user=user,job=job)
    if not applicant:
        if request.method=='POST':
            if form.is_valid():
                    instance = form.save(commit=False)
                    instance.user = user
                   
                    instance.timestamp = timezone.now()  # Set the timestamp
                    instance.save()
                    messages.success(request, 'You have saved the job as bookmark')
                    return redirect(reverse('JobApp:single_job_view', kwargs={'id': id}))    
        else:
            return redirect(reverse('JobApp:single_job_view', kwargs={'id': id}))
    else:
        messages.error(request,'You hae already saved the job')
        return redirect(reverse('JobApp:single_job_view', kwargs={'id': id}))


# Method to dashboard page whether candidate or recruieter
@login_required(login_url=reverse_lazy('Account:signin')) 
def dashboard_view(request):
    jobs=[]
    saved_jobs=[]
    applied_jobs=[]
    total_applicants={}

    if request.user.user_type == 'recruiter':
        jobs=Job.objects.filter(recruiter=request.user.id)
        for job in jobs:
            
            count=Applicant.objects.filter(job=job.id).count()
            total_applicants[job.id]=count

    if request.user.user_type =='candidate':
        saved_jobs=BookmarkJob.objects.filter(user=request.user.id)
        applied_jobs=Applicant.objects.filter(user=request.user.id)

        print(saved_jobs)
    context={
        'jobs':jobs,
        'saved_jobs':saved_jobs,
        'applied_jobs':applied_jobs,
        'total_applicants':total_applicants
    }
    

    return render(request, 'JobApp/dashboard.html', context)
    

def edit_job(request,id):
    pass

# Delete Job via recruiter
@login_required(login_url=reverse_lazy('account:login'))
# @user_is_recruiter
def delete_job(request,id):
    job=get_object_or_404(Job,id=id,recruiter=request.user.id)
    if job:
         try: 
            job.delete()
            messages.success(request,'Job Delete Successfully')
         except:
            messages.error(request,'Something went wrong while delete')
    
    return redirect('JobApp:dashboard_view')


# close the job 
@login_required(login_url=reverse_lazy('account:login'))
@user_is_recruiter
def make_close_job(request,id):
    job=get_object_or_404(Job,id=id,recruiter=request.user.id)
    if job:
        try:
            job.is_closed = True
            job.save()
            messages.success(requestr,'Job successfully closed')
        except:
               messages.warning(request,'Something went wrong') 
    return redirect('JobApp:dashboard_view')    
    
@login_required(login_url=reverse_lazy('account:login'))
@user_is_candidate
def delete_bookmark(request,id):
    bookmarkjob=get_object_or_404(BookmarkJob,id=id,user=request.user.id)
    if bookmarkjob:
        
        bookmarkjob.delete()
        messages.success(request, 'Bookmark deleted successfully')
    return redirect('JobApp:dashboard_view')        
    






def about_us(request):
    return render(request, 'JobApp/about_us.html', locals())
        

