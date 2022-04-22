#from django.urls import resolve
from django.test import TestCase
from msystem.views import MainPage
from django.http import HttpRequest
#from django.template.loader import render_to_string
#from django.urls import resolve

class HomePageTest(TestCase):

def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	
def test_responding_post_request(self):
		resp = self.client.post('/', data={'Name' :'Name'})
		self.assertIn('Name', resp.content.decode())
		self.assertInTemplateUsed(resp, 'mainpage.html')

		resp = self.client.post('/', data={'Address1' :'address'})
		self.assertIn('address', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'Age1' :'age'})
		self.assertIn('age', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'Dswd1' :'dswd'})
		self.assertIn('dswd', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')


