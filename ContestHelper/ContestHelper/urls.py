"""ContestHelper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from accounts import views as accounts_views
from Helper import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',accounts_views.welcome,name='welcome' ),
    url(r'^scriptrun/$',views.scriptrun,name='scriptrun' ),
    url(r'^problembank/',views.problembank,name='problembank' ), 
    url(r'^getproblem/',views.getproblem,name='getproblem' ), 
    url(r'^getuserinfo/(?P<pk>[.\w]+)$',views.getUserInfo,name='getuserinfo'),
    url(r'^createsection$',views.createSection,name='createsection' ), 
    url(r'^whosolved$',views.whosolved,name='whosolved' ), 
    url(r'^suggestproblem$',views.suggestproblem,name='suggestproblem' ), 
    url(r'^logout$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup$',accounts_views.signup,name='signup' ),
    url(r'^login$',accounts_views.login,name='login' ),
    url(r'^profile/(?P<pk>[.\w]+)/$',views.userprofile,name='userprofile' ),
    url(r'^section/addstudent/(?P<pk>[.\w]+)$',views.addstudent,name='addstudent'),
    url(r'^section/deletestudent/(?P<pk>[.\w]+)$',views.deletestudent,name='deletestudent'),
    url(r'^section/(?P<pk>[.\w]+)$',views.section,name='section' ),
]
