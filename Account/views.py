from django.shortcuts import render,HttpResponseRedirect ,redirect
from Account.forms import CandidateRegisteration ,CandidateProfileForm,RecruiterProfileForm 
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from Account.models import CandidateProfile ,RecruiterProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string  # Import render_to_string.......
from django.views.generic import CreateView ,TemplateView
from users.models import CustomUser
# Create your views here.

class SignUpView(TemplateView):
    template_name = 'account/signup.html'

def registration_view(request):
    """   
       candidate registration view   
    """
    if request.method == 'POST':
        form = CandidateRegisteration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Account:signin')
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
                request.session.set_expiry(0)  
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
                return redirect('Job:post_resume')
    else:
        form =AuthenticationForm()
    return render(request, 'account/login.html', {'loginform':form})
                  
def logout_view(request):
    logout(request)
    return redirect('JobApp:job_view') 

# Candidate_profile view   
def candidate_profile_view(request):
    print('ccccccccccccccccccccccccccc')
    if not request.user.is_authenticated:
        return HttpResponse('You need to logged in first to view the profile')
    try:
        profiles=CandidateProfile.objects.get(user=request.user)

    except CandidateProfile.DoesNotExist:
        return HttpResponse('Candidate Does`t have the profile')
             
    print('UserType',request.user.user_type)
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
    print('jjjjjjjjjjjjjjjjjjjj')
    if not request.user.is_authenticated:
        HttpResponse('You have to loggin first to view profile ')
    try:
        emp_profile = RecruiterProfile.objects.get(user=request.user)
    except RecruiterProfile.DoesNotExist:
        return HttpResponse('User have not recruiter profile ')  
    print('UserType',request.user.user_type) 
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
     
class  recruitersignup(CreateView):
    model = CustomUser
    form_class = RecruiterProfileForm
    template_name = 'account/recruiter_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')    

class  candidatesignup(CreateView):
    pass