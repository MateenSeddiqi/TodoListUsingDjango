from django.shortcuts import render

# Create your views here.

def signupUser(request):
    return render(request, 'todo/signupUser.html', {})