from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from shortuuidfield import ShortUUIDField
from django.urls import reverse
from django.contrib.sites.models import Site
from datetime import datetime

validar_telefono = RegexValidator(r'^(\+34|0034|34)?[ -]*(6|7|9)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')
detault_datetime = datetime(2000, 1, 1, 0, 0, 0, 0)


class Colaborador(models.Model):
    MANANA = '0'
    TARDE = '1'
    TODO_EL_DIA = '2'

    HORARIO_CHOICES = [
        (TODO_EL_DIA, 'Todo el día'),
        (MANANA, 'Mañanas'),
        (TARDE, 'Tardes'),
    ]

    geom = models.PointField(srid=4326)
    nombre = models.CharField(verbose_name='¿Cual es tu nombre?', max_length=500)
    telefono = models.CharField(blank=True, max_length=12, verbose_name='¿Cual es tu número de teléfono?', validators=[validar_telefono])
    email = models.EmailField(blank=True, verbose_name='¿Cual es tu correo electrónico?')
    horario = models.CharField(verbose_name='¿A qué horas estás disponible?', max_length=1, choices=HORARIO_CHOICES, default=TODO_EL_DIA)
    mensaje = models.TextField(help_text='Indica de qué forma puedes ayudar. Ejemplos: Realizar la compra, asistir al médico, ir a la farmacia...')
    creacion = models.DateTimeField(auto_now_add=True)

    def get_lat_js(self):
        lat_str = str(self.geom.y)
        return lat_str

    def get_lon_js(self):
        lon_str = str(self.geom.x)
        return lon_str

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'


class SolicitudAccesoColaborador(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='solicitudes_acceso')
    nombre = models.CharField(verbose_name='¿Cual es tu nombre?', max_length=500)
    telefono = models.CharField(max_length=12, verbose_name='¿Cual es tu número de teléfono?', validators=[validar_telefono])
    email = models.EmailField(verbose_name='¿Cual es tu correo electrónico?')
    mensaje = models.TextField(verbose_name='¿Qué necesitas?')
    acceso_permitido = models.BooleanField(default=False)
    codigo_acceso = ShortUUIDField()
    creacion = models.DateTimeField(auto_now_add=True)

    def get_nombre_colaborador(self):
        return self.colaborador.nombre

    def get_telefono_colaborador(self):
        return self.colaborador.telefono

    def get_email_colaborador(self):
        return self.colaborador.email

    def get_horario_colaborador(self):
        return self.colaborador.get_horario_display()

    def get_mensaje_colaborador(self):
        return self.colaborador.mensaje

    def url_autorizacion(self):
        return "http://{0}{1}?codigo={2}".format(Site.objects.get_current(), reverse("validar-acceso-colaborador"), self.codigo_acceso)

    def __str__(self):
        return self.colaborador.nombre

    class Meta:
        verbose_name = 'Petición de ayuda'
        verbose_name_plural = 'Peticiones de ayuda'
