# Generated by Django 2.2.11 on 2020-03-31 11:36

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0011_actualizado_telefono_y_correo_opcional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='telefono',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Por defecto acepta números españoles. Para añadir un número extranjero, añade el prefijo internacional', max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='solicitudaccesocolaborador',
            name='telefono',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Por defecto acepta números españoles. Para añadir un número extranjero, añade el prefijo internacional', max_length=128, region=None),
        ),
    ]
