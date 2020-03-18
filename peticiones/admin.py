from django.contrib.gis import admin
from peticiones.models import Peticion

admin.site.register(Peticion, admin.OSMGeoAdmin)
