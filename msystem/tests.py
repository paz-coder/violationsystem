
from django.test import TestCase
from django.urls import resolve
from msystem.views import MainPage
from django.http import HttpRequest

class HomePageTest(TestCase):
 def test_root_urlresolves_to_mainpage_view(self):
  found = resolve('/')
  self.assertEqual(found.func,MainPage)
 
 def test_mainpage_if_response_view(self):
  request = HttpRequest()
  response = MainPage(request)
  html = response.content.decode('utf8')
  self.assertTrue(html.startswith('<!DOCTYPE html>'))
  self.assertIn('<title>4PS MONITORING SYSTEM</title>', html)
  self.assertTrue(html.endswith('</html>'))
'''		
from django.test import TestCase
from tolsys.views import MainPage

from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve


class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response=self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')
	
	def test_mainpage_responding_view(self):
		response=self.client.get('/')
		
		request = HttpRequest()
		response = MainPage(request)
		
		html = response.content.decode('utf8')
	
		self.assertTrue(html.startswith('<!DOCTYPE html>'))
		self.assertIn('<title>4ps Monitoring System</title>',html)
		self.assertTrue(html.endswith(''))
		stringPage=render_to_string('mainpage.html')
		self.assertEqual(html,stringPage)
		self.assertTemplateUsed(response,'mainpage.html')
		
