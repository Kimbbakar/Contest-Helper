from django.db import models
from django.contrib.auth.models import User

class userinfo(models.Model):
	user = models.OneToOneField(User,related_name='userinfo',primary_key=True )
	uva  = models.CharField(max_length=20);
	school  = models.CharField(max_length=100);

class sectioninfo(models.Model):
	user = models.ForeignKey(User ,related_name='teacher',default ="00001"  , on_delete=models.CASCADE  )	
	name  = models.CharField(max_length=100);	


class sectionlist(models.Model):
	user = models.ForeignKey(User ,related_name='sections'  , on_delete=models.CASCADE  )
	role  = models.IntegerField();
	section = models.ForeignKey(sectioninfo,related_name='info',default = "00001"   , on_delete=models.CASCADE)


class problemset(models.Model):
	title  = models.CharField(max_length=100);	
	number =  models.IntegerField(primary_key = True);
	id =  models.IntegerField();
	link  = models.CharField(max_length=100);
	category  = models.IntegerField();
	difficulty = models.IntegerField();
