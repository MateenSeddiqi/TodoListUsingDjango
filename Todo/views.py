from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo


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

def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form':TodoForm()})
    else:
        try:
            form =TodoForm(request.POST)
            newtodo= form.save(commit=False)
            newtodo.user=request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form':TodoForm(), 'error': 'Bad data passed try again'})
    
def currenttodos(request):
    todos=Todo.objects.filter(user=request.user, datecompleted__isnull=True) # the first part of code will filter the todo list base on user login in website
    return render(request, 'todo/currenttodos.html', {'todos':todos})

def viewtodo(request, todo_pk):
    todo=get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=='GET':
        form=TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form})
    else:
        try:
            form=TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos') 
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form, 'error': 'Bad data passed try again'})

def completetodo(request):

