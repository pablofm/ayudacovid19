from django.contrib.gis.db import models
from django.core.validators import RegexValidator

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
    telefono = models.CharField(max_length=12, verbose_name='¿Cual es tu número de teléfono?', validators=[validar_telefono])
    email = models.EmailField(verbose_name='¿Cual es tu correo electrónico?')
    horario = models.CharField(verbose_name='¿A qué horas estás disponible?', max_length=1, choices=HORARIO_CHOICES, default=TODO_EL_DIA)
    servicios = models.TextField(help_text='Indica de qué forma puedes ayudar. Ejemplos: Realizar la compra, asistir al médico, ir a la farmacia...')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
