from django.db import models
from pessoas.models import Pessoa

class Casa(models.Model):
    valor = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    endereco = models.TextField(max_length=150, null=False, blank=False)
    dono = models.ManyToManyField(Pessoa)
