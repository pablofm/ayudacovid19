import factory
from peticiones.models import Peticion
from django.contrib.gis.geos import Point
from faker import Faker
fake = Faker('es_ES')


class PeticionFactory(factory.Factory):
    class Meta:
        model = Peticion

    geom = Point(float(fake.longitude()), float(fake.latitude()), srid=4326)
    nombre = fake.name()
    telefono = '666666666'
    email = fake.email(),
    mensaje = fake.paragraphs(nb=3)
