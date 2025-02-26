from django.shortcuts import render,HttpResponseRedirect ,redirect
from Account.forms import CandidateProfileForm,RecruiterProfileForm 
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
    form = AuthenticationForm()  # Always start with an empty form
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('JobApp:job_view')
        else:
            messages.info(request, f'account done not exit plz sign in')
    return render(request, 'account/login.html', {'loginform':form})
                  
def logout_view(request):
    logout(request)
    return redirect('JobApp:job_view') 

# Candidate_profile view   
def candidate_profile_view(request):
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
    user=request.user  # get logged in user
    recruiter_profile=get_object_or_404(RecruiterProfile,user=user)
    if request.method=='POST':
        form=RecruiterProfileForm(request.POST,instance=user) # bcz updating CustomerUser model
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            # Update RecruiterProfile fields
            recruiter_profile.company_name = form.cleaned_data.get('company_name')
            recruiter_profile.company_logo = form.cleaned_data.get('company_logo')
            recruiter_profile.contact_phone = form.cleaned_data.get('contact_phone')
            recruiter_profile.location = form.cleaned_data.get('location')
            recruiter_profile.bio = form.cleaned_data.get('bio')
            recruiter_profile.save()
    
        return redirect('Account:recruiter_profile')    
    else:
        form = RecruiterProfileForm(instance=user, initial={
            'company_name': recruiter_profile.company_name,
            'company_logo': recruiter_profile.company_logo,
            'contact_phone': recruiter_profile.contact_phone,
            'location': recruiter_profile.location,
            'bio': recruiter_profile.bio,
        })
    return render(request,"account/recruiter_update_profile_form.html", {'form':form})
     
class recruitersignup(CreateView):
    model = CustomUser
    form_class = RecruiterProfileForm
    template_name = 'account/recruiter_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # after register create job
        # return redirect('JobApp/create_job')  
        return redirect('/')  

class candidatesignup(CreateView):
    model = CustomUser
    form_class = CandidateProfileForm
    template_name = 'account/candidate_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')  