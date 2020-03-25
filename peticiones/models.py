from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from shortuuidfield import ShortUUIDField
from django.urls import reverse

validar_telefono = RegexValidator(r'^(\+34|0034|34)?[ -]*(6|7)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')


class Peticion(models.Model):
    geom = models.PointField(srid=4326)
    nombre = models.CharField(verbose_name='¿Cual es tu nombre?', max_length=500)
    telefono = models.CharField(blank=True, max_length=12, verbose_name='¿Cual es tu número de teléfono?', validators=[validar_telefono])
    email = models.EmailField(blank=True, verbose_name='¿Cual es tu correo electrónico?')
    peticion = models.TextField(help_text='Indica qué necesitas')

    def get_lat_js(self):
        lat_str = str(self.geom.y)
        return lat_str

    def get_lon_js(self):
        lon_str = str(self.geom.x)
        return lon_str

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Petición'
        verbose_name_plural = 'Peticiones'


class SolicitudAccesoPeticion(models.Model):
    peticion = models.ForeignKey(Peticion, on_delete=models.CASCADE, related_name='solicitudes_acceso')
    nombre = models.CharField(verbose_name='¿Cual es tu nombre?', max_length=500)
    telefono = models.CharField(max_length=12, verbose_name='¿Cual es tu número de teléfono?', validators=[validar_telefono])
    email = models.EmailField(verbose_name='¿Cual es tu correo electrónico?')
    mensaje = models.TextField(verbose_name='¿Cómo puedes ayudar?')
    acceso_permitido = models.BooleanField(default=False)
    codigo_acceso = ShortUUIDField()

    def get_nombre_necesitado(self):
        return self.peticion.nombre

    def get_telefono_necesitado(self):
        return self.peticion.telefono

    def get_email_necesitado(self):
        return self.peticion.email

    def get_peticion_necesitado(self):
        return self.peticion.peticion

    def url_autorizacion(self):
        return "{0}?codigo={1}".format(reverse("validar-acceso-peticion"), self.codigo_acceso)

    def __str__(self):
        return self.peticion.nombre

    class Meta:
        verbose_name = 'Solicitud de acceso'
        verbose_name_plural = 'Solicitudes de acceso'
