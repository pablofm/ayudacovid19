from django.contrib.gis import admin
from colaboradores.models import Colaborador, SolicitudAccesoColaborador


class ColaboradorAdmin(admin.OSMGeoAdmin):
    list_display = ('nombre', 'id', 'telefono', 'email', 'creacion')
    readonly_fields = ('creacion',)


class SolicitudAccesoColaboradorAdmin(admin.OSMGeoAdmin):
    exclude = ['colaborador']
    list_display = (
        'id',
        'nombre',
        'get_nombre_colaborador',
        'acceso_permitido',
        'codigo_acceso',
        'creacion',
    )

    readonly_fields = (
        'codigo_acceso',
        'url_autorizacion',
        'get_nombre_colaborador',
        'get_telefono_colaborador',
        'get_email_colaborador',
        'get_horario_colaborador',
        'get_mensaje_colaborador',
        'creacion',
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
                'creacion',
            ),
        }),
    )


admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(SolicitudAccesoColaborador, SolicitudAccesoColaboradorAdmin)
