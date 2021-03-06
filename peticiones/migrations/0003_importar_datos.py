from django.db import migrations
import os
from django.conf import settings
import csv
from django.contrib.gis.geos import Point


def importar_datos(apps, schema_editor):
    Peticion = apps.get_model('peticiones', 'Peticion')
    path = os.path.join(settings.BASE_DIR, 'peticiones/migrations/csv/plantilla_datos.csv')
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            LAT = 0
            LON = 1
            NOMBRE = 2
            TELEFONO = 3
            EMAIL = 4
            PETICION = 5
            lat = float(row[LAT])
            lon = float(row[LON])
            geom = Point(lon, lat, srid=4326)
            nombre = row[NOMBRE]
            telefono = row[TELEFONO]
            email = row[EMAIL]
            peticion = row[PETICION]
            Peticion.objects.create(geom=geom, nombre=nombre, telefono=telefono, email=email, peticion=peticion)


class Migration(migrations.Migration):

    dependencies = [
        ('peticiones', '0002_campos_no_requeridos'),
    ]

    operations = [
        migrations.RunPython(importar_datos),
    ]
