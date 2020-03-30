from peticiones import views as peticiones_views
from peticiones import views_rest as peticiones_rest
from rest_framework import routers
from django.urls import path


router = routers.SimpleRouter()
urlpatterns = [
    path('peticiones/add', peticiones_views.CrearPeticionView.as_view(), name='crear-peticion'),
    path('peticiones/<pk>/acceso', peticiones_views.SolicitarContactoPeticionView.as_view(), name='acceso-peticion'),
    path('peticiones/validar', peticiones_views.permitirContacto, name='validar-acceso-peticion'),
]

router.register('API/peticiones', peticiones_rest.APIPeticionesView)
router.register('API/peticiones/acceso', peticiones_rest.APIContactarPeticionView)

urlpatterns += router.urls
