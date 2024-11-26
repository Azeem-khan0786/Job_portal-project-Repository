from django.shortcuts import render,HttpResponseRedirect ,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from JobApp.models import  Job ,Applicant,BookmarkJob
from JobApp.forms import  JobForm , JobApplyForm ,BookmarkJobForm,ContactForm
from users.models import CustomUser
from Account.models import RecruiterProfile

from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .permission import *
import re 
import json


# from recruiters.models import Job

# import  json_file (.json) to store record of Jobs
def import_jobs(request):
    if request.method == 'POST':
        if 'json_file' not in request.FILES:
            return HttpResponse('No file uploaded.')
        json_file = request.FILES['json_file']
        data = json.load(json_file)
        for item in data:
            recruiter_instance=CustomUser.objects.get(id=item['recruiter'])
            job = Job(
                recruiter=recruiter_instance,
                title=item['title'],
                description=item['description'],
                location=item['location'],
                
                job_type=item['job_type'],
                salary=item['salary'],
                requirements=item['requirements'],
                experience_required=item['experience_required'],
                specifications=item['specifications'],
                education=item['education'],
                language=item['language'],
                schedule=item['schedule'],
                work_mode=item['work_mode'],
                created_at=item['created_at'],
                updated_at=item['updated_at'],
                is_published=item['is_published'],
                is_closed=item['is_closed'],
                Vacancy=item['Vacancy'],
                passedout=item['passedout'],
                timestamp=item['timestamp'],
                end_date=item['end_date'],
                gender=item['gender'],
                
           

                
            )
            job.save()
        return render(request, 'successjson.html')
    
    return render(request, 'loadjson.html')   

def job_view(request):
    if request.user.is_authenticated:
        if request.user.user_type=='recruiter':
            
                jobs=Job.objects.filter(recruiter=request.user)
                
        elif request.user.user_type=='candidate':
            
            jobs=Job.objects.all()
            
    else: 
        jobs=Job.objects.all()     
    for job in jobs:
      time_diff=timezone.now()-job.timestamp
      postdays=time_diff.days    
      job.skills_list = job.skills.all()[:4]
       
    return render(request, 'JobApp/jobPage.html', locals())    
   
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
    
# Details of single
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
    # Use regex to split on sentence-ending periods
    specifications_bullets = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', single_job.specifications)
    requirements_bullets = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', single_job.requirements)

    company = single_job.recruiter.recruiterprofile.company_name
    com_logo=single_job.recruiter.recruiterprofile.company_logo
    print('company_name',company)    
    context = {
        'single_job': single_job,
        'company': company,
        'com_logo': com_logo,
        'specifications_bullets':specifications_bullets,
        'requirements_bullets':requirements_bullets,

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
    
# Edit job by Recruiter

def edit_job(request,id):
    user=get_object_or_404(CustomUser,id=request.user.id)
    job=get_object_or_404(Job,id=id,recruiter=user)
    form =JobForm(instance=job)
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
         form =JobForm(request.POST,instance=job)
         if form.is_valid():
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            form.save()
            return JsonResponse({'title':title,'description':description},status=200)
            # messages.success(request, 'Job have been edit successfully')
            # return redirect('JobApp:dashboard_view')
         else:
                errors = form.errors.as_json()
                return JsonResponse({"errors": errors}, status=400)  
    
        

      
    template_name='JobApp/edit_job.html'
    return render(request, template_name, locals())
        



# Delete Job via recruiter
@login_required(login_url=reverse_lazy('account:login'))
@user_is_recruiter
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
    
# View detail of single applicant
def applicant_details(request,id):
    applicant=get_object_or_404(CustomUser,id=id)
    context={'applicant':applicant}
    template_name='JobApp/applicant_details.html'
    return render(request, template_name, context)
          

# View list of all applicants
def applicants_list(request,id):
    # user=get_object_or_404(CustomUser,user=request.user)
    all_applicants=get_list_or_404(Applicant,job=id)
    context={'all_applicants':all_applicants}
    template_name='JobApp/applicants_list.html'
    return render(request, template_name, context)

def about_us(request):
    return render(request, 'JobApp/about_us.html', locals())
def contact_us(request):
    form = ContactForm()
    # Check if the request is POST and AJAX
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse({"name": name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, 'JobApp/about_us.html', locals())
        

