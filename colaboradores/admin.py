from django.contrib.gis import admin
from colaboradores.models import Colaborador


class ColaboradorAdmin(admin.OSMGeoAdmin):
    list_display = ('geom', 'nombre', 'telefono', 'email')


admin.site.register(Colaborador, ColaboradorAdmin)
