from django.contrib.gis import admin
from comercios.models import Comercio


class ComercioAdmin(admin.OSMGeoAdmin):
    list_display = ('nombre', 'telefono', 'creacion')


admin.site.register(Comercio, ComercioAdmin)
