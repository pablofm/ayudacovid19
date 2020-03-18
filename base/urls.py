from django.urls import path
from base.views import HomeView, ColaboraView, PideView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('colabora', ColaboraView.as_view(), name='colabora'),
    path('pide', PideView.as_view(), name='pide'),

]
