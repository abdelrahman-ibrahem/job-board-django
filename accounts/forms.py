from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreation(UserCreationForm):
    username = forms.CharField(label='username')
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label='password' , widget=forms.PasswordInput())
    password2 = forms.CharField(label='check the password password' , widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1', 'password2']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password" , widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username' , 'password']