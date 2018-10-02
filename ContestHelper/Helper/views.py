import os,sys,random
SCRIPT_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.join(SCRIPT_DIR, 'script'); 
sys.path.append(SCRIPT_DIR)
  
import UVaOj

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import sectionlist,sectioninfo, problemset, solved

@login_required
def userprofile(request,pk):	
	user = get_object_or_404(User,username=pk )

	return render(request,"User_profile.html",{'user':user})

@login_required
def scriptrun(request):	
	Problems = UVaOj.getAllProblemList()
#	problemset.objects.all().delete()

	for i in Problems:
		if problemset.objects.filter(id = i['id']).exists()==False :
			obj = problemset(title = i['title'],id = i['id'],number = i['number'],category = random.randint(1,6), difficulty = random.randint(1,3)  )
			obj.save()

	return HttpResponse("Script executed successfully!!! ")


def problembank(request,pk=None):

	if pk==None:
		pk = 0

	problems = list(problemset.objects.filter(category=pk))



	return render(request,"problem_bank.html",{"Problems":problems } )

 


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




def suggestproblem(request):


	problems = list(problemset.objects.filter(category=random.randint(1,6),difficulty = random.randint(1,4) ).order_by('?')[: random.randint(5,10)] )
	
	data = {}
	data ['problem'] = []

	for i in problems:
		data['problem'].append( { 'title' : i.title,'number' : i.number,'category' : i.category, 'difficulty' : i.difficulty } )	

	return JsonResponse(data)	

 
def getUserInfo(request,pk):

	problem_list = list(problemset.objects.values())
	

	user = User.objects.get(username=pk)
	uva_solve_list = list()
 
	data = {} 


	if request.POST["update"]=='false': 
		obj = list(solved.objects.filter(user = user))

		uva_solve_list = list()

		for i in obj:
			uva_solve_list.append(i.problem.number)

		count  = {}
		count ["DP"] = 0;
		count ["Graph"] = 0;
		count ["Flow"] = 0;
		count ["Number Theory"] = 0;
		count ["String"] = 0;
		count ["Geometry"] = 0;  

		mark  = {}
		mark [1] =  "DP";
		mark [2] =  "Graph";
		mark [3] =  "Flow";
		mark [4] =  "Number Theory";
		mark [5] =  "String"; 
		mark [6] =  "Geometry";  

		problem_dict =dict()

		for i in problem_list:
			problem_dict[i["number"] ] = int (i["category"] ) 
			count[ mark[int (i["category"] ) ] ] +=1



		data ["DP"] = 0;
		data ["Graph"] = 0;
		data ["Flow"] = 0;
		data ["Number Theory"] = 0;
		data ["String"] = 0;
		data ["Geometry"] = 0; 


		for i in uva_solve_list:
			data[ mark[ problem_dict[i] ] ] +=1;




		for i in data:
			data[i]/=count[i] 
			data[i]*=10 
			data[i] = int (data[i]) + random.randint(1,6) 

	else: 	
		problem_dict =dict()

		for i in problem_list:
			problem_dict[i["id"] ] = int (i["number"] )
		uva_solve_list = UVaOj.getUserSolveList(user.userinfo.uva,problem_dict) # Problem ID

		for i in uva_solve_list:
			problem_obj = problemset.objects.get(number=i)
			if solved.objects.filter(user = request.user,problem=problem_obj ).exists()==False:
				obj = solved(user = request.user,problem=problem_obj )
				obj.save()




	data ["uva"] =  len(uva_solve_list)  


	return JsonResponse(data)	 
 