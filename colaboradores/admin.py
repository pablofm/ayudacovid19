from django.contrib.gis import admin
from colaboradores.models import Colaborador, SolicitudAccesoColaborador


class ColaboradorAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'geom', 'nombre', 'telefono', 'email')


class SolicitudAccesoColaboradorAdmin(admin.OSMGeoAdmin):
    exclude = ['colaborador']
    list_display = (
        'nombre',
        'id',
        'acceso_permitido',
        'codigo_acceso'
    )

    readonly_fields = (
        'codigo_acceso',
        'url_autorizacion',
        'get_nombre_colaborador',
        'get_telefono_colaborador',
        'get_email_colaborador',
        'get_horario_colaborador',
        'get_mensaje_colaborador',
    )

    fieldsets = (
        ('Datos del Colaborador', {
            'fields': (
                'get_nombre_colaborador',
                'get_telefono_colaborador',
                'get_email_colaborador',
                'get_horario_colaborador',
                'get_mensaje_colaborador',
                'codigo_acceso',
                'url_autorizacion',
                'acceso_permitido',
            ),
        }),
        ("Datos de quien pide ayuda", {
            'fields': (
                'nombre',
                'telefono',
                'email',
                'mensaje',
            ),
        }),
    )


admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(SolicitudAccesoColaborador, SolicitudAccesoColaboradorAdmin)
