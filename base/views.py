from django.views.generic import TemplateView
from colaboradores.models import Colaborador
from peticiones.models import Peticion
from comercios.models import Comercio


class HomeView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['colaboradores'] = Colaborador.objects.count()
        context['peticiones'] = Peticion.objects.count()
        context['comercios'] = Comercio.objects.count()
        return context


class AccesoSolicitadoView(HomeView):
    template_name = 'base/acceso_solicitado.html'


class DatosRecibidosView(HomeView):
    template_name = 'base/datos_recibidos.html'


class InformacionImportanteView(HomeView):
    template_name = 'base/informacion_importante.html'


class PeticionAtendidaView(HomeView):
    template_name = 'base/peticion_atendida.html'
