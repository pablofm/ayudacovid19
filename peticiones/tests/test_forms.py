from django.test import TestCase
from peticiones.forms import PeticionForm, ContactarPeticionForm
from peticiones.models import SolicitudAccesoPeticion
from peticiones.tests.factories import PeticionFactory
from faker import Faker
fake = Faker('es_ES')


class ColaboradorFormTest(TestCase):
    def setUp(self):
        self.datos_formulario = {
            'lat': fake.latitude(),
            'lon': fake.longitude(),
            'nombre': fake.name(),
            'email': fake.email(),
            'telefono': '666666666',
            'mensaje': fake.paragraphs(nb=3)
        }

    def test_formulario_vacio_no_es_valido(self):
        form = PeticionForm()
        self.assertFalse(form.is_valid())

    def test_formulario_sin_email_es_valido(self):
        self.datos_formulario['email'] = None
        form = PeticionForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_formulario_sin_telefono_es_valido(self):
        self.datos_formulario['telefono'] = None
        form = PeticionForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_formulario_requiere_o_telefono_o_email(self):
        self.datos_formulario['telefono'] = None
        self.datos_formulario['email'] = None
        form = PeticionForm(data=self.datos_formulario)
        self.assertFalse(form.is_valid())


class SolicitarContactoPeticionFormTest(TestCase):
    def setUp(self):
        self.peticion = PeticionFactory()
        self.peticion.save()
        self.datos_formulario = {
            'id_peticion': self.peticion.pk,
            'nombre': fake.name(),
            'telefono': '666666666',
            'email': fake.email(),
            'mensaje': fake.paragraphs(nb=3)
        }

    def test_formulario_vacio_no_es_valido(self):
        form = ContactarPeticionForm()
        self.assertFalse(form.is_valid())

    def test_formulario_sin_nombre_no_es_valido(self):
        self.datos_formulario['nombre'] = None
        form = ContactarPeticionForm(data=self.datos_formulario)
        self.assertFalse(form.is_valid())

    def test_formulario_sin_email_es_valido(self):
        self.datos_formulario['email'] = None
        form = ContactarPeticionForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_formulario_sin_telefono_no_es_valido(self):
        self.datos_formulario['telefono'] = None
        form = ContactarPeticionForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_formulario_requiere_o_telefono_o_email(self):
        self.datos_formulario['telefono'] = None
        self.datos_formulario['email'] = None
        form = ContactarPeticionForm(data=self.datos_formulario)
        self.assertFalse(form.is_valid())

    def test_formulario_con_todos_los_datos_es_valido(self):
        form = ContactarPeticionForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_tras_guardar_se_ha_creado_un_objeto(self):
        self.assertEqual(0, SolicitudAccesoPeticion.objects.count())
        form = ContactarPeticionForm(data=self.datos_formulario)
        form.save()
        self.assertEqual(1, SolicitudAccesoPeticion.objects.count())
