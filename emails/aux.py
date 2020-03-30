from django.urls import reverse
from django.contrib.sites.models import Site


def get_url_autorizacion_colaborador(codigo_acceso):
    return "http://{0}{1}?codigo={2}".format(Site.objects.get_current(), reverse("validar-acceso-colaborador"), codigo_acceso)


def get_url_autorizacion_peticion(codigo_acceso):
    return "http://{0}{1}?codigo={2}".format(Site.objects.get_current(), reverse("validar-acceso-peticion"), codigo_acceso)
