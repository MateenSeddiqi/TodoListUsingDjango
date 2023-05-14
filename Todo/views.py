from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signupUser(request):

    return render(request, 'todo/signupUser.html', {'form':UserCreationForm()})