from django.shortcuts import render ,redirect, HttpResponseRedirect
from recruiters.models import RecruiterProfile
from recruiters.forms import RecruiterProfileForm



# Recruiter Profile View
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
                