from django.shortcuts import render ,redirect, HttpResponseRedirect
from recruiters.models import RecruiterProfile


# Create your views here.
def employer_profile(request):
    emp_profile = RecruiterProfile.objects.all()  # Query to get all recruiter profiles
    return render(request, 'recruiters/employer_profile.html', {'emp_profile': emp_profile})  # Pass the queryset as context


def employer_profile_view(request):
        