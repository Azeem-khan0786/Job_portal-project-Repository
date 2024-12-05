from django.shortcuts import render,HttpResponseRedirect ,redirect
from Account.forms import CandidateRegisteration ,CandidateProfileForm,RecruiterProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from Account.models import CandidateProfile ,RecruiterProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy




# Create your views here.
def registration_view(request):
    """   
       candidate registration view
        
    """
    if request.method == 'POST':
        form = CandidateRegisteration(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('admin')
        else:
            print(form.errors)  # Add this to see form validation errors
    else:
        form = CandidateRegisteration()

    return render(request, 'account/registration.html', {'form': form})

# login page for candidates
def login_view(request):
   
    print('request.session.session_key',request.session.session_key)
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
        # Store custom data in the session
                # request.session['user_id'] = user.id
                # request.session['user_name'] = user.username
                # request.session['is_logged_in'] = True  # Custom session flag for login state
                userType=request.session['user_role'] = user.user_type  # Assuming user has 'user_type' field
                
                # Optionally set the session expiry time (e.g., session expires after 30 minutes)
                print('userType pre login',userType)
                request.session.set_expiry(None)  
                   # Session will expire after 60 sec request.session.set_expiry(60) 
                   # if  request.session.set_expiry(None) then expired when you delete manually
                   # if request.session.set_expiry(0) then expired when you close the browser
                print('userType post login',userType)
                messages.info(request,'Candidate has been loged in !')
                # return HttpResponse('hello signin')
                if user.user_type=='recruiter':
                   return redirect('JobApp:recruiter_job_view')
                else:
                    return redirect('JobApp:job_view')   
                   
            else:
                messages.warning(request,'Invalid input ')
                return redirect('Account:signout')
    else:
        form =AuthenticationForm()
    return render(request, 'account/login.html', {'loginform':form})
                  
def logout_view(request):
    logout(request)
    return redirect('JobApp:job_view') 
     



# def profile_view(request):
#     # Debugging: Print logged-in user
#     print(request.user)

#     # Ensure the user is authenticated
#     if request.user.is_authenticated:
#         # Get the CandidateProfile associated witNoneh the logged-in user
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


# Candidate_profile view   
def candidate_profile_view(request):
    profiles=CandidateProfile.objects.get(user=request.user)
    print(profiles)
    # return HttpResponse('Hekkkkko')
    return render(request,'account/candidate_profile.html',locals())                     
# Candidate_profile view update
def update_candidate_profile(request):
    try:  
        profile=CandidateProfile.objects.get(user=request.user)
    except CandidateProfile.DoesNotExist:
        profile=CandidateProfile(user=request.user)
            # candidates
        form= CandidateProfileForm(request.POST, instance=profile)
        if form.is_valid():                                                                                                                                                                                                                                      
            form.save()
            return redirect('Account:candidate_profile')
    else:
        form =CandidateProfileForm(instance=profile)
    return render(request ,'account/candidate_update_profile_form.html', {'form':form})
            
# Recruiter Profile View@id:dongli.python-preview
def recruiter_profile_view(request):
    emp_profile = RecruiterProfile.objects.get(user=request.user)
    print(emp_profile) 
    return render(request, 'account/recruiter_profile.html', {'emp_profile': emp_profile})   

# update_recruiter_profile
def update_recruiter_profile(request):
    profile=RecruiterProfile.objects.get(user=request.user)
    if request.method=='POST':
        form=RecruiterProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
        return redirect('Account:recruiter_profile')    
    else:
        form=RecruiterProfileForm(instance=profile)
    return render(request,"account/recruiter_update_profile_form.html", {'form':form})
                            

        
# @login_required(login_url=reverse_lazy('JobApp:signin'))
# def demo(request):
#     return HttpResponse('fndn')       
