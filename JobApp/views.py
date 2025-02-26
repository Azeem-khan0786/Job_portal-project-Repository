from django.shortcuts import render,HttpResponseRedirect ,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from JobApp.models import  Job ,Applicant,BookmarkJob
from JobApp.forms import  JobForm , JobApplyForm ,BookmarkJobForm,ContactForm,ResumeForm,CommentForm
from users.models import CustomUser
from django.db.models import Q
from Account.models import RecruiterProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .permission import *
import re 
import json
from rest_framework import status


# import models for Serialize data
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from JobApp.serializers import CommentSerializer
from JobApp.models import CommentModel

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
               
                
                end_date=item['end_date'],
                gender=item['gender'],
            )
            job.save()
        return render(request, 'successjson.html')
    return render(request, 'loadjson.html')   

def job_view(request):
    jobs = Job.objects.none()
    if request.user.is_authenticated:
        if request.user.user_type=='recruiter':
            jobs=Job.objects.filter(recruiter=request.user)
        elif request.user.user_type=='candidate':
            jobs=Job.objects.all()  
        else:
            jobs=Job.objects.all()     
    else: 
        jobs=Job.objects.all()    

    for job in jobs:
      time_diff=timezone.now()-job.created_at
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

# @login_required(login_url=reverse_lazy('Account:signin')) 
def single_job_view(request, id):
    """
    Provide the ability to view job details
    """ 
    single_job = get_object_or_404(Job, id=id)
    print(f"Recruiter: {single_job.recruiter} (ID: {single_job.recruiter.id})")
    recruiter=single_job.recruiter
    # Use regex to split on sentence-ending periods
    specifications_bullets = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', single_job.specifications)
    requirements_bullets = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', single_job.requirements)
    # Check if recruiter has a profile before accessing it
    if hasattr(recruiter, 'recruiterprofile'):
        company = recruiter.recruiterprofile.company_name
    else:
        company = "Company Not Available"  # Fallback value
    # company = recruiter.recruiterprofile.company_name
    com_logo=single_job.recruiter.recruiterprofile.company_logo
    comments_count=CommentModel.objects.filter(job=single_job).count()
    # use to display number of likes
   
    total_likes=single_job.total_likes()
    print('comments_count',comments_count)
    print('company_name',company)    
    context = {
        'single_job': single_job,
        'company': company,
        'comments_count':comments_count,
        'com_logo': com_logo,
        'specifications_bullets':specifications_bullets,
        'requirements_bullets':requirements_bullets,
        'total_likes':total_likes
    }
    return render(request, 'JobApp/job-single.html', context)        

# method for apply-job

@login_required(login_url=reverse_lazy('Account:signin'))      
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
                instance.created_at = timezone.now()  # Set the created_at
                instance.save()

                messages.success(request, 'You have successfully applied for this job!')
                return redirect(reverse('JobApp:single_job_view', kwargs={'id': id}))
        else:
            return redirect(reverse('JobApp:single_job_view', kwargs={'id': id}))
    
    # If already applied
    messages.warning(request, 'You have already applied for this job.')
    return redirect(reverse('JobApp:single_job_view', kwargs={'id': id}))

# method for job bookmark
@login_required(login_url=reverse_lazy('Account:signin'))      
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
                   
                    instance.created_at = timezone.now()  # Set the created_at
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

# search job via keyword, jobtitle, location
def search_job(request):
    if request.method=='POST':
        # search_query=request.POST['job','location']
        job = request.POST.get('job', '')
        location = request.POST.get('location', '')
        search_query={'job':job,'location':location}
        
        find_job=Job.objects.filter(Q(title__icontains=search_query) | Q(location__icontains=search_query))
        print(find_job)
        return render(request, 'JobApp/search_job.html', locals())
    else:
        return render(request, 'JobApp/search_job.html', {})    
        
# Edit job by Recruiter
def edit_job(request,id):
    user=get_object_or_404(CustomUser,id=request.user.id)
    job=get_object_or_404(Job,id=id,recruiter=user)
    print('user',user.id)
    print('job',job.id)
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

# method to post the resume 
@login_required(login_url=reverse_lazy('Account:signin')) 
@user_is_candidate
def post_resume(request):
    username= get_object_or_404(CustomUser,id=request.user.id)
    if request.method=='POST':
        form=ResumeForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.username=username
            instance.save()
            
            return redirect('JobApp:job_view')
    else:
        form=ResumeForm()
 
    return render(request, 'JobApp/post_resume.html', locals())


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


# if have then show otherwise submit your comment 
@login_required(login_url=reverse_lazy('Account:signin'))  
def do_comment(request,id):
    user=get_object_or_404(CustomUser,id=request.user.id)
    # user = request.user
    job = get_object_or_404(Job, id=id)
    comments = CommentModel.objects.filter(job=job).order_by('-created_at')  # Fetch job's comments
    comments_count=CommentModel.objects.filter(job=job).count()
    form = CommentForm()

    if request.method == 'POST':
        if  request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if the request is AJAX
            form = CommentForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = usercomments_count=CommentModel.objects.filter(job=job).count()
                instance.job = job
                instance.save()
                comments_count = CommentModel.objects.filter(job=job).count() 
                # Return a JSON response with the new comment details
                return JsonResponse({
                    'success': True,
                    'comment': comments,
                    'user': instance.user.email,
                    'created_at': instance.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'comments_count':comments_count
                })
            return render(request, 'comment.html', {'form': form, 'job': job, 'comments': comments})
    
    # Serialize the comments into JSON-friendly format
    comments_data = [
        { 
            'comment': c.comment,
            'user': c.user.email,
            'created_at': c.created_at.strftime('%Y-%m-%d %H:%M:%S'),
           
        }
        for c in comments
          
    ]

    return JsonResponse({'success': True, 'comments': comments_data,'comments_count':comments_count})

# method to like job 
@login_required(login_url=reverse_lazy('Account:signin'))  
def like_view(request,id):
    job= get_object_or_404(Job,id=request.POST.get('likejob'))
    if job.likes.filter(id=request.user.id).exists():
        job.likes.remove(request.user)
    else:
        job.likes.add(request.user)
    
    return  HttpResponseRedirect(reverse('JobApp:single_job_view',args=[str(id)]))
    
    

# def comment(request):
class Comments_view(APIView):
    def get(self,request ,format=None):
        comment=CommentModel.objects.all()
        serializer=CommentSerializer(comment,many=True)
        return Response(serializer.data,template_name='comment.html')
    # Get a single comment     
    def get(self,request,pk=None,format=None):
        if pk is not None:
            comment=get_object_or_404(CommentModel,pk=pk)
            serializer=CommentSerializer(comment)
            return Response(serializer.data) 

        comment=CommentModel.objects.all()
        serializer=CommentSerializer(comment,many=True)
        return Response(serializer.data)    
   
    # Post a new comment
    def post(self,request):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data':'serializer.data','status':'status.HTTP_201_CREATED'})
        return JsonResponse({'data':"serializer.errors","status":'status.HTTP_400_BAD_REQUEST'})  

    # Update specific commnet
    def put(self,request,pk=None, format=None):
        comment=get_object_or_404(CommentModel,pk=pk)
        serializer=CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)    




    # delete commentn
    def delete(self,request,pk=None,format=None):
        comment=get_object_or_404(CommentModel,pk=pk)
        comment.delete()    
        return Response(status=status.HTTP_204_NO_CONTENT)

class Commit(generics.RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    # queryset = User.objects.all()
    comment=CommentModel.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response( template_name='comment.html')