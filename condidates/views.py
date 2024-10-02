from django.shortcuts import render,HttpResponseRedirect ,redirect
from condidates.forms import CondidateRegisteration
from django.http import HttpResponse


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
