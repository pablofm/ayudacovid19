from django.contrib.gis import forms
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point
from emails.emails import enviar_correo_nuevo_comercio
from comercios.models import Comercio
from django.conf import settings


class ComercioForm(forms.ModelForm):
    lat = forms.FloatField(required=False)
    lon = forms.FloatField(required=False)

    def clean_lat(self):
        lat = self.cleaned_data['lat']
        if not lat:
            raise ValidationError("Indica donde estás")
        return lat

    def save(self, commit=True):
        comercio = super(ComercioForm, self).save(commit=False)
        comercio.geom = Point(self.cleaned_data['lon'], self.cleaned_data['lat'], srid=4326)
        comercio.fuente = settings.FUENTE
        if commit:
            comercio.save()
        enviar_correo_nuevo_comercio.delay()
        return comercio

    class Meta:
        model = Comercio
        fields = '__all__'
        exclude = ['geom', 'fuente']
