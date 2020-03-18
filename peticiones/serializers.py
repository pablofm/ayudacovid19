from peticiones.models import Peticion
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class PeticionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Peticion
        geo_field = "geom"
        fields = '__all__'
