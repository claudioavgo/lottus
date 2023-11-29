from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.nome
    
class Doacao(models.Model):
    valor = models.FloatField()
    #data = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.desc



class ItemPrestacao(models.Model):
    valor = models.FloatField()
    desc = models.TextField()

    def __str__(self):
        return self.desc

class Children(models.Model):
    nome = models.CharField(max_length=256)
    sobrenome = models.CharField(max_length=256)
    local = models.CharField(max_length=512, default="Sem informação")
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    padrinho = models.OneToOneField(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    atividades = models.ManyToManyField(Atividade, default=None, blank=True)

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=50)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    crianca = models.OneToOneField(Children, on_delete=models.DO_NOTHING, blank=True, null=True)
    crianca_autorizada = models.BooleanField(default=False)
    doacoes = models.ManyToManyField(Doacao, default=None, blank=True)

    def __str__(self):
        return self.usuario.username
