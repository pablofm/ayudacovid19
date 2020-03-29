from django.contrib.gis import admin
from colaboradores.models import Colaborador, SolicitudAccesoColaborador


class ColaboradorAdmin(admin.OSMGeoAdmin):
    list_display = ('nombre', 'id', 'telefono', 'email', 'creacion')
    readonly_fields = ('creacion',)


class SolicitudAccesoColaboradorAdmin(admin.OSMGeoAdmin):
    def nombre_colaborador(self, obj):
        return obj.colaborador.nombre

    def telefono_colaborador(self, obj):
        return obj.colaborador.telefono

    def email_colaborador(self, obj):
        return obj.colaborador.email

    def horario_colaborador(self, obj):
        return obj.colaborador.get_horario_display()

    def mensaje_colaborador(self, obj):
        return obj.colaborador.mensaje

    exclude = ['colaborador']
    list_display = (
        'id',
        'nombre',
        'nombre_colaborador',
        'acceso_permitido',
        'codigo_acceso',
        'creacion',
    )

    readonly_fields = (
        'codigo_acceso',
        'get_url_autorizacion',
        'nombre_colaborador',
        'telefono_colaborador',
        'email_colaborador',
        'horario_colaborador',
        'mensaje_colaborador',
        'creacion',
    )

    fieldsets = (
        ('Datos del Colaborador', {
            'fields': (
                'nombre_colaborador',
                'telefono_colaborador',
                'email_colaborador',
                'horario_colaborador',
                'mensaje_colaborador',
                'codigo_acceso',
                'get_url_autorizacion',
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
