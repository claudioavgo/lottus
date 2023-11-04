from lottusApp.models import *
from django.contrib.auth.models import User
from hashlib import sha256



class UserController:
    def cadastrar(email, name, cpf, phone, password):
        user = User.objects.create_user(username=name, password=password, email=email)
        Perfil.objects.create(usuario=user, cpf=cpf, telefone=phone, crianca=None, crianca_autorizada=False)
        print(user)
        return user
    
    def existe(email):
        usr = User.objects.filter(email = email).first()
        print(usr)
        if usr:
            return usr
        else:
            return False

def add_active(user, nome, desc, data):
    try:
        atv = Atividade.objects.create(nome=nome, desc=desc, data=data)
        user.atividades.add(atv)
        return True
    except Exception as e:
        print(e)
        return False

UserController.cadastrar()