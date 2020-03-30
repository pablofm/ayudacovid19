from comercios.models import Comercio
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class ComercioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Comercio
        geo_field = "geom"
        exclude = ("creacion", )
