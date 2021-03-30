from django.shortcuts import render
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm , UserCreation
# Create your views here.



def signIn(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return HttpResponseRedirect(reverse('home:index'))
    else:
        form = LoginForm()
    return render(request , 'accounts/signin.html' , {
        "form":form
    })


def signUp(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username , password=password)
            login(request , user)
            print('Create user')
            return HttpResponseRedirect(reverse('home:index'))
    else:
        form = UserCreation()
    return render(request , 'accounts/signUp.html' , {
        'userCreations':form
    })


def Logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))