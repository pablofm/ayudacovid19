from django.views.generic import TemplateView
from colaboradores.models import Colaborador
from peticiones.models import Peticion


class HomeView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['colaboradores'] = Colaborador.objects.count()
        context['peticiones'] = Peticion.objects.count()
        return context


class PeticionEnviadaView(HomeView):
    template_name = 'base/peticion_enviada.html'


class DatosRecibidosView(HomeView):
    template_name = 'base/datos_recibidos.html'
