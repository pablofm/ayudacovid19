from django.db import migrations, models
from datetime import datetime
import pytz


def populate_dates(apps, schema_editor):
    Peticion = apps.get_model('peticiones', 'Peticion')
    SolicitudAccesoPeticion = apps.get_model('peticiones', 'SolicitudAccesoPeticion')
    for peticion in Peticion.objects.all():
        peticion.creacion = datetime(2000, 1, 1, 0, 0, 0, 0, pytz.timezone('Europe/Madrid'))
        peticion.save()

    for solicitud in SolicitudAccesoPeticion.objects.all():
        solicitud.creacion = datetime(2000, 1, 1, 0, 0, 0, 0, pytz.timezone('Europe/Madrid'))
        solicitud.save()


class Migration(migrations.Migration):

    dependencies = [
        ('peticiones', '0005_peticion_a_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='peticion',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitudaccesopeticion',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.RunPython(populate_dates),
    ]
