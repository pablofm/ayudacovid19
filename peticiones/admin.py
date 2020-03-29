from django.contrib.gis import admin
from peticiones.models import Peticion, SolicitudAccesoPeticion


class PeticionAdmin(admin.OSMGeoAdmin):
    list_display = ('nombre', 'id', 'telefono', 'email', 'creacion')
    readonly_fields = ('creacion',)


class SolicitudAccesoPeticionAdmin(admin.OSMGeoAdmin):
    def nombre_necesitado(self, obj):
        return obj.peticion.nombre

    def telefono_necesitado(self, obj):
        return obj.peticion.telefono

    def email_necesitado(self, obj):
        return obj.peticion.email

    def mensaje_necesitado(self, obj):
        return obj.peticion.mensaje

    exclude = ['peticion']
    list_display = (
        'id',
        'nombre',
        'nombre_necesitado',
        'acceso_permitido',
        'codigo_acceso',
        'creacion',
    )
    readonly_fields = (
        'codigo_acceso',
        'get_url_autorizacion',
        'nombre_necesitado',
        'telefono_necesitado',
        'email_necesitado',
        'mensaje_necesitado',
        'creacion'
    )
    fieldsets = (
        ('Datos de la petición', {
            'fields': (
                'nombre_necesitado',
                'telefono_necesitado',
                'email_necesitado',
                'mensaje_necesitado',
                'codigo_acceso',
                'get_url_autorizacion',
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
