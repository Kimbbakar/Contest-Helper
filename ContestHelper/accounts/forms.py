from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    username = forms.CharField(label = 'UVa Username ', required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1', 'password2')
