from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0007_anadir_fecha_creacion'),
    ]

    operations = [
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
