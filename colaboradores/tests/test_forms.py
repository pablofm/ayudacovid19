from django.test import TestCase
from colaboradores.forms import ColaboradorForm, ContactarColaboradorForm
from colaboradores.models import SolicitudAccesoColaborador
from colaboradores.tests.factories import ColaboradorFactory
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
            'horario': '0',
            'mensaje': fake.paragraphs(nb=3)
        }

    def test_formulario_vacio_no_es_valido(self):
        form = ColaboradorForm()
        self.assertFalse(form.is_valid())

    def test_formulario_sin_email_es_valido(self):
        self.datos_formulario['email'] = None
        form = ColaboradorForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_formulario_sin_telefono_es_valido(self):
        self.datos_formulario['telefono'] = None
        form = ColaboradorForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_formulario_requiere_o_telefono_o_email(self):
        self.datos_formulario['telefono'] = None
        self.datos_formulario['email'] = None
        form = ColaboradorForm(data=self.datos_formulario)
        self.assertFalse(form.is_valid())


class SolicitarContactoColaboradorFormTest(TestCase):
    def setUp(self):
        self.colaborador = ColaboradorFactory()
        self.colaborador.save()
        self.datos_formulario = {
            'id_colaborador': self.colaborador.pk,
            'nombre': fake.name(),
            'telefono': '666666666',
            'email': fake.email(),
            'mensaje': fake.paragraphs(nb=3)
        }

    def test_formulario_vacio_no_es_valido(self):
        form = ContactarColaboradorForm()
        self.assertFalse(form.is_valid())

    def test_formulario_sin_nombre_no_es_valido(self):
        self.datos_formulario['nombre'] = None
        form = ContactarColaboradorForm(data=self.datos_formulario)
        self.assertFalse(form.is_valid())

    def test_formulario_sin_email_no_es_valido(self):
        self.datos_formulario['email'] = None
        form = ContactarColaboradorForm(data=self.datos_formulario)
        self.assertFalse(form.is_valid())

    def test_formulario_sin_telefono_no_es_valido(self):
        self.datos_formulario['telefono'] = None
        form = ContactarColaboradorForm(data=self.datos_formulario)
        self.assertFalse(form.is_valid())

    def test_formulario_requiere_o_telefono_o_email(self):
        self.datos_formulario['telefono'] = None
        self.datos_formulario['email'] = None
        form = ContactarColaboradorForm(data=self.datos_formulario)
        self.assertFalse(form.is_valid())

    def test_formulario_con_todos_los_datos_es_valido(self):
        form = ContactarColaboradorForm(data=self.datos_formulario)
        self.assertTrue(form.is_valid())

    def test_tras_guardar_se_ha_creado_un_objeto(self):
        self.assertEqual(0, SolicitudAccesoColaborador.objects.count())
        form = ContactarColaboradorForm(data=self.datos_formulario)
        form.save()
        self.assertEqual(1, SolicitudAccesoColaborador.objects.count())
