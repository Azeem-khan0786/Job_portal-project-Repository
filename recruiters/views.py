from django.shortcuts import render ,redirect, HttpResponseRedirect
from recruiters.models import RecruiterProfile

# Recruiter Profile View
def recruiter_profile_view(request):
    rec_profile = RecruiterProfile.objects.all()
    print(rec_profile) 
    return render(request, 'recruiters/recruiter_profile.html', {'emp_profile': rec_profile})   