from lottusApp.models import Perfil
from django.contrib.auth.models import User
from hashlib import sha256


class UserController:
    def cadastrar(email, name, cpf, phone, password):
        user = User.objects.create_user(email=email, username=sha256(str(name).encode("utf-8")).hexdigest(), password=password)
        Perfil.objects.create(usuario=user, cpf=cpf, telefone=phone, nome=name)
        print(user)
        return user
    
    def existe(email):
        usr = User.objects.filter(email = email).first()
        if usr:
            return usr
        else:
            return False