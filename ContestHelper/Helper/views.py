from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import sectionlist

@login_required
def userprofile(request,pk):	

	user = get_object_or_404(User,username=pk )

	return render(request,"User_profile.html",{'user':user})


def problembank(request):

	return render(request,"problem_bank.html")


def section(request):

	return render(request,"section.html")	


def contesthelper(request):

	return render(request,"contest_helper.html")	

def createSection(request):
	sectionName = request.GET['section']  
	data = {
		'sectionName': sectionName
	}

	if (sectionlist.objects.filter(name=sectionName).exists() ) :
		data['messege'] = 'Name need to be unique!!' 
	else:
		obj = sectionlist(user = request.user , name=sectionName,role = 1 )
		obj.save()
		data['messege'] = 'Section open successfully!!' 		  
		data['role'] = 1
		data['pk'] = obj.pk

	print (data['messege'])


	return JsonResponse (data)

	