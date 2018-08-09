import requests
import json

url = "http://uhunt.onlinejudge.org/"

def getUserId(userName):
    id = int(requests.get(url+"api/uname2uid/"+str(userName) ).text )
    return int(id)


def getAllProblemList():
    allProblem = requests.get(url+"api/p")
    allProblem = json.loads(allProblem.text)
    ProblemList = list() 

    for i in allProblem:
        ProblemList.append( {'id':i[0],'number':i[1],'title':i[2] } ) 

    return ProblemList

def getUserSolveList(userName,ProblemList): 

    userId = getUserId(userName)

    SolveListApi = requests.get(url+"api/solved-bits/"+str(userId))

    z = json.loads(SolveListApi.text )

    SolveList = list()

    for j in range(0,len (z[0]['solved'] ) ):
        for i in range(32):
            if (z[0]['solved'][j]&(1<<i) ):
                SolveList.append(ProblemList[32*j + i]   )

    return SolveList
