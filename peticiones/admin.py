from django.contrib.gis import admin
from peticiones.models import Peticion


class PeticionAdmin(admin.OSMGeoAdmin):
    list_display = ('geom', 'nombre', 'telefono', 'email')


admin.site.register(Peticion, PeticionAdmin)
