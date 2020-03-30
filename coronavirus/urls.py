from django.contrib import admin
from django.urls import include, path
from colaboradores import urls as colaboradores_urls
from peticiones import urls as peticiones_urls
from base import urls as base_urls
from comercios import urls as comercios_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base_urls)),
    path('', include(colaboradores_urls)),
    path('', include(peticiones_urls)),
    path('', include(comercios_urls)),
    ]

admin.site.site_header = 'Ayuda durante COVID-19'
admin.site.index_title = 'Herramientas de administración'
