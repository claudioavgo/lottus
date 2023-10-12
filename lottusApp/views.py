from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import *


# Página principal
def home(request):
    return render(request, "home/home.html")


def dashboard(request):
    return render(request, "dashboard/dash-home.html")


def login(request):
    return render(request, "auth/login.html")


def register(request):
    return render(request, "auth/register.html")


def doar(request):
    return render(request, "home/doar.html")


def apadrinhe(request):
    return render(request, "home/apadrinhe.html")


def registerPage(request):
    if request.method == "POST":
        e = User.objects.filter(email=request.POST.get("email")).count()
        if e == 0:
            user = User.objects.create_user(email=request.POST.get(
                "email"), username=request.POST.get("username"), password=request.POST.get("password"))
            Perfil.objects.create(usuario=user, cpf=request.POST.get(
                "cpf"), telefone=request.POST.get("telefone"))
            login(request, user)
        else:
            print("Email já cadastrado")
            return redirect("/register?error=1")

        return redirect("/")
    else:
        context = {"error": request.GET.get("error", 0)}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.method == "POST":
        try:
            username = User.objects.get(
                email=request.POST.get("email")).username
            user = authenticate(request, username=username,
                                password=request.POST.get("password"))

            if (user):
                login(request, user)

            return redirect("/")
        except:
            return redirect("/login?error=1")
    else:
        context = {"error": request.GET.get("error", 0)}
        return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect("/")
