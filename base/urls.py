from django.urls import path
from base import views as base_views


urlpatterns = [
    path('', base_views.HomeView.as_view(), name='index'),
    path('peticion-atendida/', base_views.PeticionAtendidaView.as_view(), name='peticion_atendida'),
    path('acceso-solicitado/', base_views.AccesoSolicitadoView.as_view(), name='acceso_solicitado'),
    path('datos-recibidos/', base_views.DatosRecibidosView.as_view(), name='datos_recibidos'),
    path('informacion-importante/', base_views.InformacionImportanteView.as_view(), name='informacion_importante'),
]
