from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Children(models.Model):
    nome = models.CharField(max_length=256)
    sobrenome = models.CharField(max_length=256)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    padrinho = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    cpf = models.CharField(max_length=14)
    telefone = models.IntegerField()
    crianca = models.OneToOneField(
        blank=True, on_delete=models.CASCADE, to=Children)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username
