from django.db import models

class Sexo(models.Model):
    SEXOS = [('F', 'Feminino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(choices=SEXOS, max_length=10)