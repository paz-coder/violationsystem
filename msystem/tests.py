from django.test import TestCase
from msystem.views import MainPage

class HomePageTest(TestCase):

	def test_mainpage_as_seen_client(self):
		resp = self.client.get('/')
		self.assertTemplateUsed(resp, 'mainpage.html')
	
	def test_responding_post_request(self):
		resp = self.client.post('/', data={'Name' :'Name'})
		self.assertIn('Name', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'address' :'Address'})
		self.assertIn('Address', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'age' :'Age'})
		self.assertIn('Age', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'dswd' :'Dswd'})
		self.assertIn('Dswd', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')

		resp = self.client.post('/', data={'member' :'Member'})
		self.assertIn('Member', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')



