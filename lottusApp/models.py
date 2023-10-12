from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Children(models.Model):
    nome = models.CharField(max_length=256)
    sobrenome = models.CharField(max_length=256)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    padrinho = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome