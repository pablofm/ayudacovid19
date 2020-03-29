from peticiones.models import Peticion, SolicitudAccesoPeticion
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class PeticionSerializer(GeoFeatureModelSerializer):
    identificador = serializers.SerializerMethodField()

    def get_identificador(self, obj):
        return obj.pk

    class Meta:
        model = Peticion
        geo_field = "geom"
        fields = ['nombre', 'mensaje', 'identificador']


class SolicitudAccesoPeticionSerializer(serializers.ModelSerializer):
    # peticion = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = SolicitudAccesoPeticion
        exclude = ("acceso_permitido", "codigo_acceso", "creacion")
