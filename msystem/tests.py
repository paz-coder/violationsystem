from django.test import TestCase
from msystem.views import MainPage



class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		resp =self.client.post('/', data= {
		'Name': 'juan j',
		'address' : 'san antonio',
		'age' :'40',
		'dswd' : '0011',
		})
		self.assertEqual(Member.objects.count(), 1)
		Mem = Member.objects.first()
		self.assertEqual(Mem.Name , 'juan j')
		self.assertEqual(Mem.Address , 'san antonio')
		self.assertEqual(Mem.Age , '40')
		self.assertEqual(Mem.Dswd , '0011')


	def test_redirect_POST(self):
		response = self.client.post('/', data={ 
		'Name': 'juan j',
		'address' : 'san antonio',
		'age' :'40',
		'dswd' : '0011',
        })
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Member.objects.count(), 0)


class ORMTest(TestCase):
 	def test_saving_retrieving_list(self):
 		list1 = Member()
 		list1.Name = 'juan'
 		list1.Address  = 'san antonio'
 		list1.Age = '40'
 		list1.Dswd ='0011'
 		list1.save()

 		list2 = Member()
 		list2.Name = 'john b'
 		list2.Address  = 'san carlos'
 		list2.Age = '30'
 		list2.Dswd ='0022'
 		list2.save()

 		items = Member.objects.all()
 		self.assertEqual(items.count(), 2)
 		items1 = items[0]
 		items2 = items[1]


 		self.assertEqual(items2.Name , 'juan j')
		self.assertEqual(items2.Address , 'san antonio')
		self.assertEqual(items2.Age , '40')
		self.assertEqual(items2.Dswd , '0011')

 		self.assertEqual(items1.Name , 'john b')
		self.assertEqual(items1.Address , 'san carlos')
		self.assertEqual(items1.Age , '30')
		self.assertEqual(items1.Dswd , '0022')


	def test_template_displays_list(self):
 		Member.objects.create(Name='juan j',
 			Address='san antonio',
 			Age='40', 
 			Dswd='0011',)

 		Member.objects.create(Name='john b',
 			Address='san carlos',
 			Age='30', 
 			Dswd='0022',)
 		response = self.client.get('/')
 		self.assertIn('1: juan j san antonio 40 0011', response.content.decode())
 		self.assertIn('2: john b san carlos 30 0022', response.content.decode())

'''class HomePageTest(TestCase):

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
		self.assertIn('dswd', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')

		resp = self.client.post('/', data={'member' :'Member'})
		self.assertIn('Member', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')'''


          
     



