from fuentes.models import Fuente


def actualizar_fuente(key):
    if key:
        if Fuente.objects.filter(key=key).count():
            fuente = Fuente.objects.get(key=key)
            fuente.contador += 1
            fuente.save()
