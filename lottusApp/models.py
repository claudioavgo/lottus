from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Children(models.Model):
    nome = models.CharField(max_length=256)
    sobrenome = models.CharField(max_length=256)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    padrinho = models.OneToOneField(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=50)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    crianca = models.OneToOneField(Children, on_delete=models.DO_NOTHING, blank=True, null=True)
    crianca_autorizada = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.username
