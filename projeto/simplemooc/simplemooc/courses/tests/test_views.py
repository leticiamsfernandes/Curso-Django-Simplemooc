from django.test import TestCase
from django.core import mail
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings

from simplemooc.courses.models import Course

class ContactCourseTestCase(TestCase):
	
	"""
	toda vez que um teste é chamado irá executar
	o setup e o teardown
	"""
	# antes de cada teste
	def setUp(self):
		self.course = Course.objects.create(
			name='Django',
			slug='django'
			)

	# depois de cada teste
	def tearDown(self):
		self.course.delete()

	#quando se inicializa uma classe toda de testes
	"""@classmethod
	# antes de todas as execuções
	def setUpClass(cls):
		pass

	# depois de todas as execuções
	def tearDownClass(cls):
		pass"""

	def test_contact_form_error(self):
		data = {'name': 'Fulano de Tal',
		'email': '',
		'message': ''}
		client = Client()
		path = reverse('courses:details', 
			args=[self.course.slug])
		response = client.post(path, data)
		self.assertFormError(response, 
			'form', 'email', 
			'Este campo é obrigatório.')
		self.assertFormError(response, 
			'form', 'message', 
			'Este campo é obrigatório.')

	def test_contact_form_success(self):
		data = {'name': 'Fulano de Tal',
		'email': 'email@email.com',
		'message': 'Oi'}
		client = Client()
		path = reverse('courses:details', 
			args=[self.course.slug])
		response = client.post(path, data)
		self.assertEqual(mail.outbox[0].to, 
			[settings.CONTACT_EMAIL])

