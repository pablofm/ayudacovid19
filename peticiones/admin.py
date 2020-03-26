from django.contrib.gis import admin
from peticiones.models import Peticion, SolicitudAccesoPeticion


class PeticionAdmin(admin.OSMGeoAdmin):
    list_display = ('nombre', 'id', 'telefono', 'email', 'creacion')
    readonly_fields = ('creacion',)


class SolicitudAccesoPeticionAdmin(admin.OSMGeoAdmin):
    exclude = ['peticion']
    list_display = (
        'nombre',
        'id',
        'acceso_permitido',
        'codigo_acceso',
        'creacion',
    )
    readonly_fields = (
        'codigo_acceso',
        'url_autorizacion',
        'get_nombre_necesitado',
        'get_telefono_necesitado',
        'get_email_necesitado',
        'get_mensaje_necesitado',
        'creacion'
    )
    fieldsets = (
        ('Datos de la petición', {
            'fields': (
                'get_nombre_necesitado',
                'get_telefono_necesitado',
                'get_email_necesitado',
                'get_mensaje_necesitado',
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
                'creacion',
            ),
        }),
    )


admin.site.register(Peticion, PeticionAdmin)
admin.site.register(SolicitudAccesoPeticion, SolicitudAccesoPeticionAdmin)
