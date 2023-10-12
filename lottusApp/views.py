from django.shortcuts import render
from django.http import HttpResponse

# Página principal
def home(request):
    return render(request, "home/home.html")

def dashboard(request):
    return render(request, "dashboard/dash-home.html")

def login(request):
    return render(request, "auth/login.html")

def register(request):
    return render(request, "auth/register.html")