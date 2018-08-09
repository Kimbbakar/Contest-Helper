import os,sys
SCRIPT_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.join(SCRIPT_DIR, 'script'); 
sys.path.append(SCRIPT_DIR)

from UVaOj import getUserId 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class signupform(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    first_name = forms.CharField(label = 'Name ',max_length=200, required=True )
    uva = forms.CharField(label = 'UVa Username ',max_length=20, required=True)
    school = forms.CharField(label = 'School ',max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username','first_name',  'email','school','uva', 'password1', 'password2')
        exclude = ['last_name']

    def clean_username(self):
        data = self.cleaned_data['username']

        if getUserId(data)==0:
            raise forms.ValidationError("Username is invalid!")   

        return data

