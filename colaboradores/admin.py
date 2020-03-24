from django.contrib.gis import admin
from colaboradores.models import Colaborador, SolicitudAccesoColaborador


class ColaboradorAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'geom', 'nombre', 'telefono', 'email')


class SolicitudAccesoColaboradorAdmin(admin.OSMGeoAdmin):
    list_display = ('nombre', 'id', 'acceso_permitido', 'codigo_acceso')
    readonly_fields = ('codigo_acceso', 'url_autorizacion', )


admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(SolicitudAccesoColaborador, SolicitudAccesoColaboradorAdmin)
