from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from requests import request

def login_view(request):
    if request.method == "GET":
        return render(request, template_name="user_app/login.html")
    elif request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next = request.GET.get('next')
            if next is not None:
               return HttpResponseRedirect("next")
            return HttpResponseRedirect("/")  
        return HttpResponseRedirect("/auth/login/")

def logout_view(request):
    logout(request)
    return render(request, template_name="user_app/logout.html")