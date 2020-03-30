from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from comercios.models import Comercio
from comercios.forms import ComercioForm


class CrearComercioView(CreateView):
    template_name = 'comercios/add.html'
    form_class = ComercioForm
    model = Comercio
    success_url = reverse_lazy('datos_recibidos')
