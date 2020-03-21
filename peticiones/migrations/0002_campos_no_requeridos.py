import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peticiones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peticion',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='¿Cual es tu correo electrónico?'),
        ),
        migrations.AlterField(
            model_name='peticion',
            name='telefono',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator('^(\\+34|0034|34)?[ -]*(6|7)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')], verbose_name='¿Cual es tu número de teléfono?'),
        ),
    ]
