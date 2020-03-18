from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from colaboradores.models import Colaborador
from colaboradores.forms import ColaboradorForm


class HomeView(TemplateView):
    template_name = 'base/index.html'


class ColaboraView(CreateView):
    template_name = 'base/colaborador_form.html'
    form_class = ColaboradorForm
    model = Colaborador
    success_url = '/'
