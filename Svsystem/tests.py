from django.test import TestCase
from Svsystem.views import MainPage
from Svsystem.models import Stundentinfo
#from django.http import HttpRequest
#from django.template.loader import render_to_string
#from django.urls import resolve

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		resp =self.client.post('/', data= {
		'studentName': 'Paz, Eldren',
		'ID' : 'TUPC-18-0696',
		'Section' :'4B',
		'Violation' : 'Cheating',
		})
		self.assertEqual(Stundentinfo.objects.count(), 1)
		newEntry = Stundentinfo.objects.first()
		self.assertEqual(newEntry.Sname , 'Paz, Eldren')
		self.assertEqual(newEntry.Sid , 'TUPC-18-0696')
		self.assertEqual(newEntry.Ssection , '4B')
		self.assertEqual(newEntry.Sviolation , 'Cheating')


	def test_redirect_POST(self):
		response = self.client.post('/', data={ 
		'studentName': 'Paz, Eldren',
		'ID' : 'TUPC-18-0696',
		'Section' :'4B',
		'Violation' : 'Cheating',
        })
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Stundentinfo.objects.count(), 0)


class ORMTest(TestCase):
 	def test_saving_retrieving_list(self):
 		entry1 = Stundentinfo()
 		entry1.Sname = 'Paz, Eldren'
 		entry1.Sid  = 'TUPC-18-0696'
 		entry1.Ssection = '4B'
 		entry1.Sviolation ='Cheating'
 		entry1.save()

 		entry2 = Stundentinfo()
 		entry2.Sname = 'Ryan, Balota'
 		entry2.Sid  = 'TUPC-18-0696'
 		entry2.Ssection = '4B'
 		entry2.Sviolation ='Noisy'
 		entry2.save()

 		items = Stundentinfo.objects.all()
 		self.assertEqual(items.count(), 2)
 		items1 = items[0]
 		items2 = items[1]


 		self.assertEqual(items2.Sname , 'Ryan, Balota')
		self.assertEqual(items2.Sid , 'TUPC-18-0696')
		self.assertEqual(items2.Ssection , '4B')
		self.assertEqual(items2.Sviolation , 'Cheating')

 		self.assertEqual(items1.Sname , 'Paz, Eldren')
		self.assertEqual(items1.Sid , 'TUPC-18-0696')
		self.assertEqual(items1.Ssection , '4B')
		self.assertEqual(items1.Sviolation , 'Noisy')


	def test_template_displays_list(self):
 		Stundentinfo.objects.create(Sname='Paz, Eldren',
 			Sid='TUPC-18-0696',
 			Ssection='4B', 
 			Sviolation='Cheating',)

 		Stundentinfo.objects.create(Sname='Ryan, Balota',
 			Sid='TUPC-18-0696',
 			Ssection='4B', 
 			Sviolation='Noisy',)
 		response = self.client.get('/')
 		self.assertIn('1: Paz, Eldren TUPC-18-0696 4B Cheating', response.content.decode())
 		self.assertIn('2: Ryan, Balota TUPC-18-0623 4B Noisy', response.content.decode())

