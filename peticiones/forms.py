from django.contrib.gis import forms
from peticiones.models import Peticion
from peticiones.models import SolicitudAccesoPeticion
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point
from emails.emails import enviar_correo_ofreciendo_ayuda
from emails.emails import enviar_correo_nueva_peticion
from emails.emails import enviar_correo_nueva_solicitud_peticion
from django.conf import settings


class PeticionForm(forms.ModelForm):
    lat = forms.FloatField(required=False)
    lon = forms.FloatField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        telefono = cleaned_data.get("telefono")
        email = cleaned_data.get("email")
        if not email and not telefono:
            raise ValidationError("Es necesario un método de contacto: email o teléfono")

    def clean_lat(self):
        lat = self.cleaned_data['lat']
        if not lat:
            raise ValidationError("Indica donde estás")
        return lat

    def is_valid(self):
        valid = super(PeticionForm, self).is_valid()
        if not valid:
            return valid
        if not self.data["email"] and not self.data["telefono"]:
            return False
        return True

    def save(self, commit=True):
        peticion = super(PeticionForm, self).save(commit=False)
        peticion.geom = Point(self.cleaned_data['lon'], self.cleaned_data['lat'], srid=4326)
        peticion.fuente = settings.FUENTE
        if commit:
            peticion.save()
        enviar_correo_nueva_peticion.delay()
        return peticion

    class Meta:
        model = Peticion
        fields = '__all__'
        exclude = ['geom', 'fuente']


class ContactarPeticionForm(forms.ModelForm):
    id_peticion = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        telefono = cleaned_data.get("telefono")
        email = cleaned_data.get("email")
        if not email and not telefono:
            raise ValidationError("Es necesario un método de contacto: email o teléfono")

    def is_valid(self):
        valid = super(ContactarPeticionForm, self).is_valid()
        if not valid:
            return valid
        if not self.data["email"] and not self.data["telefono"]:
            return False
        return True

    def save(self):
        contacto = super(ContactarPeticionForm, self).save(commit=False)
        contacto.peticion = Peticion.objects.get(pk=self.cleaned_data['id_peticion'])
        contacto.fuente = settings.FUENTE
        contacto.save()
        # Se envía un correo donde alquien quiere ayuda a una persona necesitada y solicita el acceso a sus datos.
        enviar_correo_nueva_solicitud_peticion.delay()
        enviar_correo_ofreciendo_ayuda.delay(contacto.pk)
        return contacto

    class Meta:
        model = SolicitudAccesoPeticion
        fields = '__all__'
        exclude = ['peticion', 'codigo_acceso', 'acceso_permitido', 'fuente']
