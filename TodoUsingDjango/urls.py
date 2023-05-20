"""TodoUsingDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth urls
    path('signup/', views.signupUser, name='signupUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('login/', views.loginUser, name='loginUser'),

    #TOdo urls 
    path('', views.Home, name='Home'),
    path('current/', views.currenttodos, name='currenttodos'),
    path ('create/', views.createtodo, name='createtodo'),
    path ('completed/', views.completedtodos, name='completedtodos'),
    path ('todo/<int:todo_pk>', views.viewtodo, name='todoview'),
    path ('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path ('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo')
]
