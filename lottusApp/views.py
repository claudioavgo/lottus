from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .models import *

from .utils import *

def requer_autenticacao(f):
    def dec(request, *args, **kwargs):
        # Verifica session['logado']
        if (request.user.is_authenticated):
            username = request.user

            usr = Perfil.objects.get(usuario=User.objects.get(username=username))
            print(usr)
        else:
            usr = None

        return f(request, user=usr, *args, **kwargs)
    return dec

# Página principal
@requer_autenticacao
def home(request, user):
    context = {
        'user': user,
    }
    return render(request, "home/home.html", context)

@requer_autenticacao
def dashboard(request, user):
    context = {
        'user': user,
    }
    return render(request, "dashboard/dash-home.html", context)

@requer_autenticacao
def doar(request, user):
    context = {
        'user': user,
    }
    return render(request, "home/doar.html", context)

@requer_autenticacao
def apadrinhe(request, user):
    context = {
        'user': user,
    }
    return render(request, "home/apadrinhe.html", context)


def register(request):
    if request.method == "POST":
        if not UserController.existe(email=request.POST.get("email")):
            user = UserController.cadastrar(
                cpf=request.POST.get("cpf"), 
                email=request.POST.get("email"),
                name=request.POST.get("username"),
                password=request.POST.get("password"),
                phone=request.POST.get("telefone")
            )

            login(request, user)
        else:
            print("Email já cadastrado")
            return redirect("/cadastro?error=1")

        return redirect("/")
    else:
        context = {"error": request.GET.get("error", 0)}
        return render(request, 'auth/register.html', context)


def loginPage(request):
    if request.method == "POST":
        try:
            print(request.POST.get("email"))
            username = UserController.existe(email=request.POST.get("email")).username
            user = authenticate(request, username=username, password=request.POST.get("password"))

            if (user):
                login(request, user)

            return redirect("/")
        except Exception as e:
            print(e)
            return redirect("/login?error=1")
    else:
        context = {"error": request.GET.get("error", 0)}
        return render(request, 'auth/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect("/")
