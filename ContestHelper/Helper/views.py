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
#   problemset.objects.all().delete()

    for i in Problems:
        if problemset.objects.filter(id = i['id']).exists()==False :
            obj = problemset(title = i['title'],id = i['id'],number = i['number'])
            obj.save()

    return HttpResponse("Script executed successfully!!! ")

## need to fix it

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
    if (    User.objects.filter(username = student).exists()==False ):
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
 
    cur_section = sectioninfo.objects.get(pk = request.POST['section'] )

    student = list()

    for i in cur_section.info.all():
        if i.role == 0: 
            student.append(i.user)

    solved_problem = list(solved.objects.filter(user__in=student).values_list('problem', flat=True).distinct() ) 

    problems = list()

    if request.POST['coach'] == "1":
        coach_solve = list(solved.objects.filter(user=cur_section.user).values_list('problem',flat=True))
        problems = list(problemset.objects.exclude(number__in =solved_problem  ).order_by('?') )
        tmp = list()
        "not a good solution, But sqllite can't handle big query"
        for i in problems:
            if i.number in coach_solve:
                tmp.append(i)
        problems = tmp[:5] ;
    else:
        problems = list(problemset.objects.exclude(number__in =solved_problem  ).order_by('?')[:5] )

    data = {}
    data ['problem'] = []
    data['section'] = cur_section.name

    for i in problems:
        data['problem'].append( { 'title' : i.title,'number' : i.number,  'difficulty' : i.difficulty } )    

    return JsonResponse(data)   

## need to work on this function
 
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

    else:   
        problem_dict =dict()

        for i in problem_list:
            problem_dict[i["id"] ] = int (i["number"] )
        uva_solve_list = UVaOj.getUserSolveList(user.userinfo.uva,problem_dict) # Problem ID

        for i in uva_solve_list:
            problem_obj = problemset.objects.get(number=i)
            if solved.objects.filter(user = user,problem=problem_obj ).exists()==False:
                obj = solved(user = user,problem=problem_obj )
                obj.save()


    NOT_CATEGORIZE = "NONE"
    DP = 'DP'
    GRAPH = 'GRAPH'
    STRING = 'STRING'
    NT = 'NT'
    GEO = "GEO"

    TOPIC_LIST = (
        (NOT_CATEGORIZE , "NONE"),
        (DP, 'Dynamic Programming'),
        (GRAPH, 'Graph Theory'),
        (STRING, 'String'),
        (NT, 'Number Theory'),
        (GEO, 'Geometry'),
    )



    for i in TOPIC_LIST:
        Total = solved.objects.filter(topic=i[0] ).values_list('problem',flat=True).distinct() .count()
        individual = solved.objects.filter(user =user , topic=i[0] ).values_list('problem',flat=True).count()
        data[i[0] ] = (individual * 10.0)

        if Total>0:
            data[i[0] ] = data[i[0] ]/Total
 

    data ["uva"] =  len(uva_solve_list)  


    return JsonResponse(data)    
 

def whosolved(request):

    data = {}
    cur_section = sectioninfo.objects.get(pk=request.POST['section_pk'] )
    cur_problem = problemset.objects.get(number = request.POST['id'])
    data ["name"] = cur_section.name 
    data ["solver"] = []

    # need to check from which online judge
    # need to check problem id is valid or not

    for i in cur_section.info.all():
        if solved.objects.filter(user = i.user,problem = cur_problem ).exists()==True:
            data["solver"].append({"username":i.user.username} )

    return JsonResponse(data)