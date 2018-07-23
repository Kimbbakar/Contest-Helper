from django.shortcuts import render,redirect
from django.http import HttpResponse

def userprofile(request):

	return render(request,"User_profile.html")


def problembank(request):

	return render(request,"problem_bank.html")


def section(request):

	return render(request,"section.html")	


def contesthelper(request):

	return render(request,"contest_helper.html")	