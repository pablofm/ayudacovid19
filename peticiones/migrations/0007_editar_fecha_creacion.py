from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peticiones', '0006_anadir_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peticion',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='solicitudaccesopeticion',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
