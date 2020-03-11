from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField()
    datanascimento = models.DateField(null=True)
    email = models.EmailField(null=True)