from lottusApp.models import Perfil
from django.contrib.auth.models import User
from hashlib import sha256


class UserController:
    def cadastrar(email, name, cpf, phone, password):
        user = User.objects.create_user(username=sha256(str(name).encode("utf-8")).hexdigest(), password=password)
        user.email = email
        Perfil.objects.create(usuario=user, cpf=cpf, telefone=phone, nome=name)
        print(user)
        return user
    
    def existe(email):
        usr = User.objects.filter(email = email).first()
        print(usr)
        if usr:
            return usr
        else:
            return False