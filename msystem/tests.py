from django.urls import resolve
from django.test import TestCase
from msystem.views import MainPage
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve

class HomePageTest(TestCase):

def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	
def test_responding_post_request(self):
		resp = self.client.post('/', data={'newname' :'NewName'})
		self.assertIn('NewName', resp.content.decode())
		self.assertInTemplateUsed(resp, 'mainpage.html')
def test_responding_post_request(self):
		resp = self.client.post('/', data={'add' :'Newaddress'})
		self.assertIn('Newaddress', resp.content.decode())
		self.assertInTemplateUsed(resp, 'mainpage.html')

