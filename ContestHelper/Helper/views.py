from django.shortcuts import render,redirect
from django.http import HttpResponse

def userprofile(request):

	return render(request,"User_profile.html")