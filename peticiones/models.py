from django.contrib.gis.db import models
from shortuuidfield import ShortUUIDField
from phonenumber_field.modelfields import PhoneNumberField


class Peticion(models.Model):
    geom = models.PointField(srid=4326)
    nombre = models.CharField(verbose_name='¿Cual es tu nombre?', max_length=500)
    telefono = PhoneNumberField(blank=True, help_text='Por defecto acepta números españoles. Para añadir un número extranjero, añade el prefijo internacional')
    email = models.EmailField(blank=True, verbose_name='¿Cual es tu correo electrónico?')
    mensaje = models.TextField(help_text='Indica qué necesitas')
    creacion = models.DateTimeField(auto_now_add=True)
    atendida = models.BooleanField(default=False)
    fuente = models.CharField(max_length=25, default="???")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Petición'
        verbose_name_plural = 'Peticiones'


class SolicitudAccesoPeticion(models.Model):
    peticion = models.ForeignKey(Peticion, on_delete=models.CASCADE, related_name='solicitudes_acceso')
    nombre = models.CharField(verbose_name='¿Cual es tu nombre?', max_length=500)
    telefono = PhoneNumberField(blank=True, help_text='Por defecto acepta números españoles. Para añadir un número extranjero, añade el prefijo internacional')
    email = models.EmailField(blank=True, verbose_name='¿Cual es tu correo electrónico?')
    mensaje = models.TextField(verbose_name='¿Cómo puedes ayudar?')
    acceso_permitido = models.BooleanField(default=False)
    codigo_acceso = ShortUUIDField()
    creacion = models.DateTimeField(auto_now_add=True)
    fuente = models.CharField(max_length=25, default="???")

    def __str__(self):
        return self.peticion.nombre

    class Meta:
        verbose_name = 'Oferta de colaboración'
        verbose_name_plural = 'Ofertas de colaboración'
