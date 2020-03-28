from django.db import models
from shortuuidfield import ShortUUIDField


class Fuente(models.Model):
    key = ShortUUIDField()
    fuente = models.CharField(max_length=500)
    accion = models.CharField(max_length=500)
    contador = models.IntegerField(default=0)
