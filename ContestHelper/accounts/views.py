from django.contrib.auth import login as auth_login 
from django.shortcuts import render, redirect
from .forms import signupform

def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = signupform()
    return render(request, 'signup.html', {'form': form})
 

def welcome(request):
    return render(request,'welcome.html');