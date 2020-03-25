from django.contrib.gis import admin
from peticiones.models import Peticion, SolicitudAccesoPeticion


class PeticionAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'geom', 'nombre', 'telefono', 'email')


class SolicitudAccesoPeticionAdmin(admin.OSMGeoAdmin):
    exclude = ['peticion']
    list_display = (
        'nombre',
        'id',
        'acceso_permitido',
        'codigo_acceso'
    )
    readonly_fields = (
        'codigo_acceso',
        'url_autorizacion',
        'get_nombre_necesitado',
        'get_telefono_necesitado',
        'get_email_necesitado',
        'get_peticion_necesitado'
    )
    fieldsets = (
        ('Datos de la petición', {
            'fields': (
                'get_nombre_necesitado',
                'get_telefono_necesitado',
                'get_email_necesitado',
                'get_peticion_necesitado',
                'codigo_acceso',
                'url_autorizacion',
                'acceso_permitido',
            ),
        }),
        ("Datos del colaborador", {
            'fields': (
                'nombre',
                'telefono',
                'email',
                'mensaje',
            ),
        }),
    )


admin.site.register(Peticion, PeticionAdmin)
admin.site.register(SolicitudAccesoPeticion, SolicitudAccesoPeticionAdmin)
