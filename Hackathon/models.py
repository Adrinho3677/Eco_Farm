from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    nascimento = models.DateField(null=False)

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=100)
    nascimento = models.DateField(null=False)

    def __str__(self):
        return self.nome

class Maquina(models.Model):

    TIPO = [
        ('Trator', 'Trator'),
        ('Colheitadeira', 'Colheitadeira'),
        ('Plantadeira', 'Plantadeira'),
        ('Pulverizador', 'Pulverizador'),
    ]

    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100, choices=TIPO)
    modelo = models.CharField(max_length=200)
    ano = models.CharField(max_length=6)

    def __str__(self):
        return self.nome

class Semente(models.Model):

    TIPO = [
        ('Milho', 'Milho'),
        ('Soja', 'Soja'),
    ]

    tipo = models.CharField(max_length=100, choices=TIPO)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.tipo

class TarefaMaquina(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_inicio = models.DateTimeField(null=False)

    def __str__(self):
        return self.descricao

class TarefaFuncionario(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_inicio = models.DateTimeField(null=False)

    def __str__(self):
        return self.descricao