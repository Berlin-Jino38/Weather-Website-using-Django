from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MyCustomForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password '}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re_Enter your password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']