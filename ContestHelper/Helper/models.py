from django.db import models
from django.contrib.auth.models import User

class userinfo(models.Model):
	user = models.OneToOneField(User,related_name='userinfo',primary_key=True )
	uva  = models.CharField(max_length=20);
	school  = models.CharField(max_length=100);