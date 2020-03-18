from django.contrib import admin
from colaboradores import urls as colaboradores_urls
from base import urls as base_urls
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base_urls)),
    path('', include(colaboradores_urls)),
    ]

admin.site.site_header = 'Ayuda durante COVID-19'
admin.site.index_title = 'Herramientas de administración'
