from django.db import migrations
import os
from django.conf import settings
import csv
from django.contrib.gis.geos import Point



def importar_datos(apps, schema_editor):
    Colaborador = apps.get_model('colaboradores', 'Colaborador')
    path = os.path.join(settings.BASE_DIR, 'colaboradores/migrations/csv/sevilla.csv')
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            LAT = 0
            LON = 1
            NOMBRE = 2
            HORARIO = 3
            TELEFONO = 4
            EMAIL = 5
            SERVICIOS = 6
            print("LAT =>"+row[LAT])
            print("LON =>"+row[LON])
            lat = float(row[LAT])
            lon = float(row[LON])
            geom = Point(lon, lat, srid=4326)
            nombre = row[NOMBRE]
            horario = row[HORARIO]
            telefono = row[TELEFONO]
            email = row[EMAIL]
            servicios = row[SERVICIOS]
            Colaborador.objects.create(geom=geom, nombre=nombre, telefono=telefono, email=email, servicios=servicios, horario=horario)


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0002_campos_no_requeridos'),
    ]

    operations = [
        migrations.RunPython(importar_datos),
    ]
