from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from shortuuidfield import ShortUUIDField
from django.urls import reverse
from django.contrib.sites.models import Site

validar_telefono = RegexValidator(r'^(\+34|0034|34)?[ -]*(6|7|9)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')


class Peticion(models.Model):
    geom = models.PointField(srid=4326)
    nombre = models.CharField(verbose_name='¿Cual es tu nombre?', max_length=500)
    telefono = models.CharField(blank=True, max_length=12, verbose_name='¿Cual es tu número de teléfono?', validators=[validar_telefono])
    email = models.EmailField(blank=True, verbose_name='¿Cual es tu correo electrónico?')
    mensaje = models.TextField(help_text='Indica qué necesitas')
    creacion = models.DateTimeField(auto_now_add=True)

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
    creacion = models.DateTimeField(auto_now_add=True)

    def get_url_autorizacion(self):
        return "http://{0}{1}?codigo={2}".format(Site.objects.get_current(), reverse("validar-acceso-peticion"), self.codigo_acceso)

    def __str__(self):
        return self.peticion.nombre

    class Meta:
        verbose_name = 'Oferta de colaboración'
        verbose_name_plural = 'Ofertas de colaboración'
