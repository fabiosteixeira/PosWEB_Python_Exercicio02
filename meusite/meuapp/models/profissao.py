from django.db import models

class Profissao(models.Model):
    nome = models.CharField(max_length=50)
    mediasalario = models.FloatField()