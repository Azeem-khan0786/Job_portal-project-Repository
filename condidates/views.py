from django.shortcuts import render,HttpResponseRedirect ,redirect
from condidates.forms import CondidateRegisteration
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
def registration(request):
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
def Login(request):
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
                return redirect('signout')
    else:
        form =AuthenticationForm()
    return render(request, 'Condidates/login.html', {'loginform':form})
                  
def signout(request):
    logout(request)
    return redirect('login') 
     


def custom_csrf_failure(request, reason=""):
    return render(request, "csrf_failure.html", {"reason": reason})
                      