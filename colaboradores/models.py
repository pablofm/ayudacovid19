from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from shortuuidfield import ShortUUIDField
from django.urls import reverse


validar_telefono = RegexValidator(r'^(\+34|0034|34)?[ -]*(6|7)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')


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
    servicios = models.TextField(help_text='Indica de qué forma puedes ayudar. Ejemplos: Realizar la compra, asistir al médico, ir a la farmacia...')

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
    mensaje = models.TextField(verbose_name='Indica brevemente como podrían ayudarte:')
    acceso_permitido = models.BooleanField(default=False)
    codigo_acceso = ShortUUIDField()

    def __str__(self):
        return self.colaborador.nombre

    def url_autorizacion(self):
        return "{0}?codigo={1}".format(reverse("validar-acceso-colaborador"), self.codigo_acceso)

    class Meta:
        verbose_name = 'Solicitud de acceso'
        verbose_name_plural = 'Solicitudes de acceso'
