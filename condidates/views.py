from django.shortcuts import render,HttpResponseRedirect ,redirect
from condidates.forms import CondidateRegisteration ,ProfileForm
from condidates.models import CondidateProfile
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



# Create your views here.
def registration_view(request):
    if request.method == 'POST':
        form = CondidateRegisteration(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('admin')
        else:
            print(form.errors)  # Add this to see form validation errors
    else:
        form = CondidateRegisteration()

    return render(request, 'Condidates/registration.html', {'form': form})

# login page for condidates
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
                messages.info(request,'Condidate has been loged in !')
                # return HttpResponse('hello signin')
                return redirect('/admin/')
            else:
                messages.warning(request,'Invalid input ')
                return redirect('condidates:signout')
    else:
        form =AuthenticationForm()
    return render(request, 'Condidates/login.html', {'loginform':form})
                  
def logout_view(request):
    logout(request)
    return redirect('condidates:signin') 
     


def custom_csrf_failure(request, reason=""):
    return render(request, "csrf_failure.html", {"reason": reason})
                      
def profile_view(request):
    if request.method=='POST':
       form=ProfileForm(request.POST,instance=request.user)
       if form.is_valid():
           form.save()
           return redirect('condidates:signout')
    else:
        form= ProfileForm(instance=request.user)
    return render(request,'Condidates/ProfileAdd.html',locals())      
def my_profile(request):
    profile=CondidateProfile.objects.all()
    return render(request,'Condidates/profilePage.html',locals())                      