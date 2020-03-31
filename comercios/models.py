from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Comercio(models.Model):
    geom = models.PointField(srid=4326)
    nombre = models.CharField(verbose_name='Nombre del comercio', max_length=500)
    telefono = PhoneNumberField(blank=True, help_text='Por defecto acepta números españoles. Para añadir un número extranjero, añade el prefijo internacional')
    mensaje = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Comercio'
        verbose_name_plural = 'Comercios'
