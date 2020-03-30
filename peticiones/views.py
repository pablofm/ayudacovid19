from peticiones.models import Peticion, SolicitudAccesoPeticion
from django.views.generic.edit import CreateView
from peticiones.forms import PeticionForm, ContactarPeticionForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from emails.emails import enviar_correo_acceso_datos


class CrearPeticionView(CreateView):
    template_name = 'peticiones/add.html'
    form_class = PeticionForm
    model = Peticion
    success_url = reverse_lazy('datos_recibidos')


class SolicitarContactoPeticionView(CreateView):
    template_name = 'peticiones/contactar.html'
    form_class = ContactarPeticionForm
    success_url = reverse_lazy('peticion_enviada')

    def get_context_data(self, **kwargs):
        context = super(SolicitarContactoPeticionView, self).get_context_data(**kwargs)
        context['peticion'] = get_object_or_404(Peticion, pk=self.kwargs['pk'])
        return context


def permitirContacto(request):
    permitido = False
    nombre = None
    solicitud = None
    codigo = request.GET.get('codigo')

    if SolicitudAccesoPeticion.objects.filter(codigo_acceso=codigo).exists():
        solicitud = SolicitudAccesoPeticion.objects.get(codigo_acceso=codigo)

    if solicitud:
        solicitud.acceso_permitido = True
        solicitud.save()
        permitido = True
        nombre = solicitud.nombre

        # La persona necesitada da permiso para compartir sus datos. Se envían 2 correos:
        # El primero para el colaborador, con los datos de la persona que necesita ayuda
        datos_email_colaborador = {
            'nombre_para': solicitud.nombre,
            'email_para': solicitud.email,
            'nombre_contacto': solicitud.peticion.nombre,
            'telefono_contacto': solicitud.peticion.telefono,
            'email_contacto': solicitud.peticion.email,
            'mensaje_contacto': solicitud.peticion.mensaje
        }
        enviar_correo_acceso_datos.delay(datos_email_colaborador)

        # El segundo para la persona necesitada, con los datos de la persona que le ofrece ayuda
        datos_email_solicitante = {
            'nombre_para': solicitud.peticion.nombre,
            'email_para': solicitud.peticion.email,
            'nombre_contacto': solicitud.nombre,
            'telefono_contacto': solicitud.telefono,
            'email_contacto': solicitud.email,
            'mensaje_contacto': solicitud.mensaje
        }
        enviar_correo_acceso_datos.delay(datos_email_solicitante)

    return render(request, 'base/validar_codigo.html', {"nombre": nombre, "permitido": permitido})
