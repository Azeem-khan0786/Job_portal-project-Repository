from django.shortcuts import render ,redirect, HttpResponseRedirect
from recruiters.models import RecruiterProfile, Job
from recruiters.forms import RecruiterProfileForm



# Recruiter Profile View@id:dongli.python-preview
def recruiter_profile_view(request):
    emp_profile = RecruiterProfile.objects.get(user=request.user)
    print(emp_profile) 
    return render(request, 'recruiters/recruiter_profile.html', {'emp_profile': emp_profile})   

# update_recruiter_profile
def update_recruiter_profile(request):
    profile=RecruiterProfile.objects.get(user=request.user)
    if request.method=='POST':
        form=RecruiterProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
        return redirect('recruiters:recruiter_profile')    
    else:
        form=RecruiterProfileForm(instance=profile)
    return render(request,"recruiters/update_profile_form.html", {'form':form})
                
                
def job_view(request):
    jobs=Job.objects.filter(recruiter=request.user)
    return render(request, 'recruiters/jobPage.html', {'jobs':jobs})
    
# post your job on candidate site
def post_job(request):
    postJob=Job.objects.filter(recruiter=request.user)
    template_name='candidates/jobPage.html'
    return render(request, template_name, {'postJob':postJob})
        
    
    
    
   