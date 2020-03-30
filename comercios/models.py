from django.contrib.gis.db import models
from django.core.validators import RegexValidator


validar_telefono = RegexValidator(r'^(\+34|0034|34)?[ -]*(6|7|9)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')


class Comercio(models.Model):
    geom = models.PointField(srid=4326)
    nombre = models.CharField(verbose_name='Nombre del comercio', max_length=500)
    telefono = models.CharField(blank=True, max_length=12, verbose_name='Número de teléfono', validators=[validar_telefono])
    mensaje = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Comercio'
        verbose_name_plural = 'Comercios'
