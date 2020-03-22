from peticiones.models import Peticion
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers


class PeticionSerializer(GeoFeatureModelSerializer):
    identificador = serializers.SerializerMethodField()

    def get_identificador(self, obj):
        return "P-{}".format(obj.pk)

    class Meta:
        model = Peticion
        geo_field = "geom"
        fields = '__all__'
