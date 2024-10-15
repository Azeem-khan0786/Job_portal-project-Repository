from django.shortcuts import render,HttpResponseRedirect ,redirect
from candidates.forms import CandidateRegisteration ,CandidateProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import CandidateProfile 
from recruiters.models import Job


def home(request,form=''):
    postJob=Job.objects.all()
    template_name='candidates/jobPage.html'
    # return render(request, 'home.html', )
    return render(request, template_name, {'postJob':postJob})
    
    

    

# Create your views here.
def registration_view(request):
    if request.method == 'POST':
        form = CandidateRegisteration(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('admin')
        else:
            print(form.errors)  # Add this to see form validation errors
    else:
        form = CandidateRegisteration()

    return render(request, 'candidates/registration.html', {'form': form})

# login page for candidates
def login_view(request):
    if request.method=='POST':
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            
            user=authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user is not None:
                login(request,user)
                print(request,user)
                messages.info(request,'Candidate has been loged in !')
                # return HttpResponse('hello signin')
                return redirect('candidates:candidate_profile')
            else:
                messages.warning(request,'Invalid input ')
                return redirect('candidates:signout')
    else:
        form =AuthenticationForm()
    return render(request, 'candidates/login.html', {'loginform':form})
                  
def logout_view(request):
    logout(request)
    return redirect('candidates:signin') 
     


def custom_csrf_failure(request, reason=""):
    return render(request, "csrf_failure.html", {"reason": reason})
# def profile_view(request):
#     # Debugging: Print logged-in user
#     print(request.user)

#     # Ensure the user is authenticated
#     if request.user.is_authenticated:
#         # Get the CandidateProfile associated with the logged-in user
#         user_profile = request.user.CandidateProfile

#         if request.method == 'POST':
#             form = CandidateProfileForm(request.POST, instance=user_profile)  # Pass the CandidateProfile instance
#             if form.is_valid():
#                 form.save()
#                 return redirect('candidates:my_profile')  # Redirect after successful save
#         else:
#             form = CandidateProfileForm(instance=user_profile)  # Pass the CandidateProfile instance for pre-filling the form

#         # Render the profile add template with the form
#         return render(request, 'candidates/ProfileAdd.html', {'form': form})  # Use dictionary for context
#     else:
#         # Handle the case where the user is not authenticated
#         return redirect('login')  # Redirect to login page or show an error
   
def candidate_profile_view(request):
    profiles=CandidateProfile.objects.all()
    return render(request,'candidates/profilePage.html',locals())                     

def update_candidate_profile(request):
    try:  
        profile=CandidateProfile.objects.get(user=request.user)
    except CandidateProfile.DoesNotExist:
        profile=CandidateProfile(user=request.user)
            
    if request.method=='POST':
        form= CandidateProfileForm(request.POST, instance=profile)
        if form.is_valid():                                                                                                                                                                                                                                      
            form.save()
            return redirect('candidates:candidate_profile')
    else:
        form =CandidateProfileForm(instance=profile)
    return render(request ,'candidates/update_profile_form.html', {'form':form})
            
            
    