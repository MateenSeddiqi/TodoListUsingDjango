from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def Home(request):
    return render(request, 'todo/Home.html')

def signupUser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupUser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user =User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save() 
                login (request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupUser.html', {'form':UserCreationForm(), 'error': 'User name is already taken please add new one'}) 

        else:
            return render(request, 'todo/signupUser.html', {'form':UserCreationForm(), 'error': 'Password is not match please check'})   

def logoutUser(request):
    if request.method=='POST':
        logout(request)
        return redirect('Home')


def loginUser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginUser.html', {'form':AuthenticationForm()})
    else:
        user =authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginUser.html', {'form':AuthenticationForm(), 'error':'User name or password did not match'})
        else:
            login (request, user)
            return redirect('currenttodos')


def currenttodos(request):
    return render(request, 'todo/currenttodos.html', {})

