from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import sectionlist,sectioninfo

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

	if (sectioninfo.objects.filter(name=sectionName).exists() ) :
		data['messege'] = 'Name need to be unique!!' 
	else:
		section_obj = sectioninfo(user = request.user,name = sectionName ) 
		section_obj.save()
		obj = sectionlist(user = request.user , section=section_obj,role = 1 )
		obj.save()

		data['messege'] = 'Section open successfully!!' 		  
		data['role'] = 1
		data['pk'] = section_obj.pk

	return JsonResponse (data)

def section(request,pk):
	section_pk = sectioninfo.objects.get(pk = pk)

	return render(request,"section.html", {'section_pk': section_pk} )


def addstudent(request,pk):

	if(sectionlist.objects.filter(user=request.user).exists()==False ):
		return redirect("userprofile",request.user.pk )

	section_now = sectioninfo.objects.get(pk = pk)
	student = request.GET['student']
	data = {
		"messege": "!!"
	}
	if (	User.objects.filter(username = student).exists()==False ):
		data["messege"] = "This student does not exist!!"
	else:
		user = User.objects.get(username=student)

		if(section_now.user!=request.user) :
			data["messege"] = "You can not add student in this section!"

		elif sectionlist.objects.filter(user = user,section=section_now).exists()==True:
			data["messege"] = "This member already exist!!"
		else:
			obj = sectionlist(user=user,role=0,section = section_now)
			obj.save()
			data["student"] = user.first_name
			data["messege"] = "Student has been added!!"
			data["pk"] = user.username
	return JsonResponse(data)


def deletestudent(request,pk):

	if(sectionlist.objects.filter(user=request.user).exists()==False ):
		return redirect("userprofile",request.user.pk )

	section_now = sectioninfo.objects.get(pk = pk)
	student = request.GET['student']
	data = {
		"messege": "!!"
	}

	user = User.objects.get(username=student)

	if(section_now.user!=request.user) :
		data["messege"] = "You can not delete student in this section!"

	else:
		obj = sectionlist.objects.get(user=user,role=0,section = section_now)
		obj.delete()
		data["messege"] = "Student has been deleted!!"

	return JsonResponse(data)	


	