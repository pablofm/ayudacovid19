from django.urls import path
from base import views as base_views


urlpatterns = [
    path('', base_views.HomeView.as_view(), name='index'),
    path('solicitud_enviada/', base_views.PeticionEnviadaView.as_view(), name='peticion_enviada'),
    path('datos_decibidos/', base_views.DatosRecibidosView.as_view(), name='datos_recibidos'),
    path('informacion_importante/', base_views.InformacionImportanteView.as_view(), name='informacion_importante'),
]
