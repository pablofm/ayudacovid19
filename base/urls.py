from django.urls import path
from base import views as base_views


urlpatterns = [
    path('', base_views.HomeView.as_view(), name='index'),
    path('colaborador/', base_views.ColaboradorView.as_view(), name='colaborador-add'),
    path('peticion/', base_views.PeticionView.as_view(), name='peticion-add'),

]
