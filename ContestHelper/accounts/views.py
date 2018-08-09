from django.contrib.auth import login as auth_login 
from django.shortcuts import render, redirect
from .forms import signupform, LogInForm
from Helper.models import userinfo
from django.contrib.auth import authenticate  

def signup(request):
    if request.user.is_authenticated:
        return redirect('userprofile',pk = request.user.username )

    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.save()
            userinfo.objects.create(user=user,uva=form['uva'].value(),school =form['school'].value() )
            auth_login(request, user)
            return redirect('userprofile',pk = user.username )
        else :
            return render(request, 'signup.html', {'form': form})
    else: 
        form = signupform()
        return render(request, 'signup.html', {'form': form})
 

def welcome(request):
    return render(request,'welcome.html');

def login(request):
    if request.user.is_authenticated:
        return redirect('userprofile',pk = request.user.username )
    
    Warning = 0

    if request.method=='POST':
        form = LogInForm(request.POST)

        if form.is_valid():            
            user = authenticate(request, username=form['username'].value(), password=form['password'].value() )
            if user is not None:
                auth_login(request,user)
                return redirect('userprofile',pk = request.user.username )
            else:
                Warning = 1
        else: 
            Warning = 2 
    else: 
        form = LogInForm()

    return render(request,'login.html',{'form':form , 'Warning':Warning } )