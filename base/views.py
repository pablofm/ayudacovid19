from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from colaboradores.models import Colaborador
from colaboradores.forms import ColaboradorForm
from peticiones.models import Peticion
from peticiones.forms import PeticionForm


class HomeView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['colaboradores'] = Colaborador.objects.count()
        context['peticiones'] = Peticion.objects.count()
        return context


class ColaboraView(CreateView):
    template_name = 'base/colaborador_form.html'
    form_class = ColaboradorForm
    model = Colaborador
    success_url = '/'


class PideView(CreateView):
    template_name = 'base/peticion_form.html'
    form_class = PeticionForm
    model = Peticion
    success_url = '/'
