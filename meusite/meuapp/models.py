from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField()
    datanascimento = models.DateField(null=True)
    email = models.EmailField(null=True)

class Profissao(models.Model):
    nome = models.CharField(max_length=50)
    mediasalario = models.FloatField()

class Sexo(models.Model):
    SEXOS = [('F', 'Feminino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(choices=SEXOS, max_length=10)