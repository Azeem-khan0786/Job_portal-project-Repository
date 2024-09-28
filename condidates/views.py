from django.shortcuts import render

# Create your views here.
def registration(request):
    # if request.method=='POST':
    #     form=CondidateRegisteration(request.POST)
    #     if form.is_valid():
    #         user=form.save()
    form=CondidateRegisteration()
    return render(request,'Condidates/registration.html',{'form':form})