from peticiones.models import Peticion, SolicitudAccesoPeticion
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class PeticionListSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Peticion
        geo_field = "geom"
        fields = ['nombre', 'mensaje', 'id']


class PeticionSerializer(PeticionListSerializer):
    class Meta:
        model = Peticion
        geo_field = "geom"
        exclude = ("creacion", )


class SolicitudAccesoPeticionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudAccesoPeticion
        exclude = ("acceso_permitido", "codigo_acceso", "creacion")
