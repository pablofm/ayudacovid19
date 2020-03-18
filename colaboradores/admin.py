from django.contrib.gis import admin
from colaboradores.models import Colaborador

admin.site.register(Colaborador, admin.OSMGeoAdmin)
