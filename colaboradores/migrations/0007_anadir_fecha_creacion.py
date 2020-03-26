from django.db import migrations, models
from datetime import datetime
import pytz


def populate_dates(apps, schema_editor):
    Colaborador = apps.get_model('colaboradores', 'Colaborador')
    SolicitudAccesoColaborador = apps.get_model('colaboradores', 'SolicitudAccesoColaborador')
    for peticion in Colaborador.objects.all():
        peticion.creacion = datetime(2000, 1, 1, 0, 0, 0, 0, pytz.timezone('Europe/Madrid'))
        peticion.save()

    for solicitud in SolicitudAccesoColaborador.objects.all():
        solicitud.creacion = datetime(2000, 1, 1, 0, 0, 0, 0, pytz.timezone('Europe/Madrid'))
        solicitud.save()


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0006_servicios_a_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitudaccesocolaborador',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.RunPython(populate_dates),
        migrations.AlterField(
            model_name='colaborador',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='solicitudaccesocolaborador',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),

    ]
