from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def signupUser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupUser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
        else:
            print("Hello ")