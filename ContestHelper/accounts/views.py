from django.contrib.auth import login as auth_login 
from django.shortcuts import render, redirect
from .forms import signupform
from Helper.models import userinfo
 

def signup(request):
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