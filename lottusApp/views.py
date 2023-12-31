import random

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import *
from .utils import *


def requer_autenticacao(f):
    def dec(request, *args, **kwargs):
        if (request.user.is_authenticated):
            username = request.user

            usr = Perfil.objects.get(
                usuario=User.objects.get(username=username))
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


@requer_autenticacao
def register(request, user):
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
        context = {"error": request.GET.get("error", 0), "user": user}
        return render(request, 'auth/register.html', context)


@requer_autenticacao
def loginPage(request, user):
    if request.method == "POST":
        try:
            print(request.POST.get("email"))
            username = UserController.existe(email=request.POST.get("email"))
            if not username:
                raise Exception("O usuário não existe")
            user = authenticate(request, username=username,
                                password=request.POST.get("password"))

            if (user):
                login(request, user)

            return redirect("/")
        except Exception as e:
            print(e)
            return redirect("/login?error=1")
    else:
        context = {"error": request.GET.get("error", 0), "user": user}
        return render(request, 'auth/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect("/")

# Páginas do dashboard


@requer_autenticacao
def dash_crianca(request, user):
    context = {
        'user': user,
        'more':  {"criancas": Children.objects.all(), "usuarios": Perfil.objects.all()} if user.usuario.is_staff else False,
    }
    return render(request, "dashboard/dash-children.html", context)


@requer_autenticacao
def dashboard(request, user):
    context = {
        'user': user,
        'more':  {"criancas": Children.objects.all(), "usuarios": Perfil.objects.all()} if user.usuario.is_staff else False,
    }
    return render(request, "dashboard/dash-home.html", context)


@requer_autenticacao
def contrato(request, user):
    context = {
        'user': user,
        'more':  {"criancas": Children.objects.all(), "usuarios": Perfil.objects.all()} if user.usuario.is_staff else False,
    }
    return render(request, "dashboard/contract-page.html", context)


@requer_autenticacao
def dash_doacoes(request, user):
    if request.method == "POST":
        valor = request.POST.get("valor")
        doa = Doacao.objects.create(valor=float(valor), desc="a")
        user.doacoes.add(doa)
        return redirect("/dashboard/doacoes")
    else:
        context = {
            'user': user,
            'more':  {"criancas": Children.objects.all(), "usuarios": Perfil.objects.all()} if user.usuario.is_staff else False,
        }
        return render(request, "dashboard/dash-doacoes.html", context)


@requer_autenticacao
def dash_specific_child(request, user, nome):
    crianca = Children.objects.filter(nome=nome).first()
    context = {
        'user': user,
        'more':  {"criancas": Children.objects.all(), "usuarios": Perfil.objects.all()} if user.usuario.is_staff else False,
        'crianca': crianca,
        'padrinho': Perfil.objects.filter(usuario=crianca.padrinho).first()

    }
    return render(request, "dashboard/dash-specific-child.html", context)


@requer_autenticacao
def dash_specific_user(request, user, nome):
    usr = User.objects.filter(username=nome).first()
    usr_perfil = None

    for i in Perfil.objects.all():
        if i.usuario == usr:
            usr_perfil = i

    context = {
        'user': user,
        'more':  {"criancas": Children.objects.all(), "usuarios": Perfil.objects.all()} if user.usuario.is_staff else False,
        'usuario': usr_perfil
    }
    return render(request, "dashboard/dash-specific-user.html", context)


@requer_autenticacao
def dash_add_child(request, user):
    if request.method == "POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        local = request.POST.get("local")
        idade = request.POST.get("idade")
        data_nascimento = request.POST.get("data")

        Children.objects.create(nome=nome, sobrenome=sobrenome,
                                local=local, idade=idade, data_nascimento=data_nascimento)

        return redirect("/dashboard/adicionar/crianca")
    else:
        context = {
            'user': user,
            'more':  {"criancas": Children.objects.all(), "usuarios": Perfil.objects.all()} if user.usuario.is_staff else False,
        }
        return render(request, "dashboard/dash-add-child.html", context)


@requer_autenticacao
def dash_add_activity(request, user):
    if request.method == "POST":
        nome = request.POST.get("nome")
        data = request.POST.get("data")
        desc = request.POST.get("desc")
        crianca_nome = request.GET.get('crianca')

        atv = Atividade.objects.create(nome=nome, desc=desc, data=data)

        ch = Children.objects.filter(nome=crianca_nome).first()

        ch.atividades.add(atv)

        return redirect(f"/dashboard/crianca/{ch}")
    else:
        context = {
            'user': user,
            'more':  {"criancas": Children.objects.all(), "usuarios": Perfil.objects.all()} if user.usuario.is_staff else False,
        }
        return render(request, "dashboard/dash-add-activity.html", context)


@requer_autenticacao
def dash_random_child(request, user):
    if not user:
        return redirect(f"/cadastro")

    try:
        if user.crianca and user.crianca_autorizada:
            return redirect(f"/dashboard")
        elif user.crianca:
            return redirect(f"/dashboard/contrato")
    except:
        print("Não possui criança")

    criancas = Children.objects.all()

    choosed_child = random.choice(criancas)

    crianca = Children.objects.filter(nome=str(choosed_child)).first()
    crianca.padrinho = user.usuario

    crianca.save()

    user.crianca = choosed_child
    user.save()

    return redirect(f"/dashboard/contrato")


@requer_autenticacao
def dash_aprovar_contrato(request, user, crianca):
    ch = Children.objects.filter(nome=crianca).first()
    padrinho = Perfil.objects.filter(usuario=ch.padrinho).first()

    padrinho.crianca_autorizada = True
    padrinho.save()

    return redirect(f"/dashboard/crianca/{crianca}")

# Empresa


@requer_autenticacao
def empresa(request, user):
    context = {
        'user': user,
    }
    return render(request, "home/empresa.html", context)


@requer_autenticacao
def empresa_info(request, user):
    context = {
        'user': user,
    }
    return render(request, "home/empresa-info.html", context)


@requer_autenticacao
def diaadiadogotas(request, user):
    context = {
        'user': user,
    }
    return render(request, "home/diaadiadogotas.html", context)


@requer_autenticacao
def iniciativasdogotas(request, user):
    context = {
        'user': user,
    }
    return render(request, "home/iniciativasdogotas.html", context)


@requer_autenticacao
def configuracoes(request, user):

    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("telefone")
        username = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        
        user.usuario.username = username
        user.usuario.save()
        user.usuario.email = email
        user.usuario.save()
        user.telefone = telefone
        user.save()

        #Perfil.objects.get(cpf=user["cpf"])
        return redirect('/dashboard/configuracoes')
    
    context = {
        'user': user,
    }
    
    print()

    return render(request, "dashboard/configuracoes.html", context)


@requer_autenticacao
def dashcontas(request, user):
    if request.method == "POST":
        valor = request.POST.get("valor")
        descricao = request.POST.get("descricao")

        Valor.objects.create(valor=valor, desc=descricao)

        return redirect('/dashboard/dashcontas')
    
    context = {
        'user': user,
        'contas': Valor.objects.all()
    }

    return render(request, "dashboard/dashcontas.html", context)

@requer_autenticacao
def criancas(request, user):
    criancas = Children.objects.all()

    context = {
        'user': user,
        'criancas': criancas    
    }
    
    return render(request, "dashboard/criancas.html", context)

@requer_autenticacao
def usuarios(request, user):
    usuarios = Perfil.objects.all()

    context = {
        'user': user,
        'usuarios': usuarios
    }
    
    return render(request, "dashboard/usuarios.html", context)

@requer_autenticacao
def add_admin(request, user, usuario):


    usr = User.objects.filter(username=usuario).first()

    usr.is_staff = True
    usr.save()

    return redirect(f"/dashboard/user/{usuario}")