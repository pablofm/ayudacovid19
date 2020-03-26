# Generated by Django 2.2.11 on 2020-03-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peticiones', '0004_solicitudaccesopeticion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitudaccesopeticion',
            options={'verbose_name': 'Solicitud de acceso', 'verbose_name_plural': 'Solicitudes de acceso'},
        ),
        migrations.RenameField(
            model_name='peticion',
            old_name='peticion',
            new_name='mensaje',
        ),
        migrations.AlterField(
            model_name='solicitudaccesopeticion',
            name='mensaje',
            field=models.TextField(verbose_name='¿Cómo puedes ayudar?'),
        ),
    ]
