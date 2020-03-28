from django.contrib import admin
from fuentes.models import Fuente


class FuenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'fuente', 'accion', 'contador')
    readonly_fields = ('contador',)


admin.site.register(Fuente, FuenteAdmin)
