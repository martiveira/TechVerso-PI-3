from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    habilidades = models.TextField()

class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    requisitos = models.TextField()

class Candidatura(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

