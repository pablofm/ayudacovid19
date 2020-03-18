from django.contrib.gis.db import models
from django.core.validators import RegexValidator

validar_telefono = RegexValidator(r'^(\+34|0034|34)?[ -]*(6|7)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')


class Peticion(models.Model):
    geom = models.PointField(srid=4326)
    nombre = models.CharField(verbose_name='¿Cual es tu nombre?', max_length=500)
    telefono = models.CharField(max_length=12, verbose_name='¿Cual es tu número de teléfono?', validators=[validar_telefono])
    email = models.EmailField(verbose_name='¿Cual es tu correo electrónico?')
    peticion = models.TextField(help_text='Indica qué necesitas')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Petición'
        verbose_name_plural = 'Peticiones'
