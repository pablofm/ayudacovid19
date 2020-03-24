from django.contrib.gis import admin
from peticiones.models import Peticion, SolicitudAccesoPeticion


class PeticionAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'geom', 'nombre', 'telefono', 'email')


class SolicitudAccesoPeticionAdmin(admin.OSMGeoAdmin):
    list_display = ('nombre', 'id', 'acceso_permitido', 'codigo_acceso')
    readonly_fields = ('codigo_acceso', 'url_autorizacion', )


admin.site.register(Peticion, PeticionAdmin)
admin.site.register(SolicitudAccesoPeticion, SolicitudAccesoPeticionAdmin)
