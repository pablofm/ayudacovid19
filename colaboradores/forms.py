from django.contrib.gis import forms
from colaboradores.models import Colaborador
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point


class ColaboradorForm(forms.ModelForm):
    lat = forms.FloatField(required=False)
    lon = forms.FloatField(required=False)

    def clean_lat(self):
        lat = self.cleaned_data['lat']
        if not lat:
            raise ValidationError("Indica donde estás")
        return lat

    def save(self, commit=True):
        m = super(ColaboradorForm, self).save(commit=False)
        m.geom = Point(self.cleaned_data['lon'], self.cleaned_data['lat'], srid=4326)
        if commit:
            m.save()
        return m

    class Meta:
        model = Colaborador
        fields = '__all__'
        exclude = ['geom']
