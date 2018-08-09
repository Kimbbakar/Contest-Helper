from django.db import models
from django.contrib.auth.models import User

class onlinejudgeid(models.Model):
	user = models.OneToOneField(User,related_name='ojid',primary_key=True )
	uva  = models.CharField(max_length=20);