from django.contrib.gis.db import models
from shortuuidfield import ShortUUIDField
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

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
    telefono = PhoneNumberField(blank=True, help_text='Por defecto acepta números españoles. Para añadir un número extranjero, añade el prefijo internacional')
    email = models.EmailField(blank=True, verbose_name='¿Cual es tu correo electrónico?')
    horario = models.CharField(verbose_name='¿A qué horas estás disponible?', max_length=1, choices=HORARIO_CHOICES, default=TODO_EL_DIA)
    mensaje = models.TextField(help_text='Indica de qué forma puedes ayudar. Ejemplos: Realizar la compra, asistir al médico, ir a la farmacia...')
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'


class SolicitudAccesoColaborador(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='solicitudes_acceso')
    nombre = models.CharField(verbose_name='¿Cual es tu nombre?', max_length=500)
    telefono = PhoneNumberField(blank=True, help_text='Por defecto acepta números españoles. Para añadir un número extranjero, añade el prefijo internacional')
    email = models.EmailField(blank=True, verbose_name='¿Cual es tu correo electrónico?')
    mensaje = models.TextField(verbose_name='¿Qué necesitas?')
    acceso_permitido = models.BooleanField(default=False)
    codigo_acceso = ShortUUIDField()
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.colaborador.nombre

    class Meta:
        verbose_name = 'Petición de ayuda'
        verbose_name_plural = 'Peticiones de ayuda'
