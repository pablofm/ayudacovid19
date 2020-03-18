from django.urls import path
from base.views import HomeView, ColaboraView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('colabora', ColaboraView.as_view(), name='colabora'),
]
