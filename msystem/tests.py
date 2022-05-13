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
		self.assertIn('dswd', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')

		resp = self.client.post('/', data={'member' :'Member'})
		self.assertIn('Member', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')

class ORM(TestCase):

   def test_saving_and_retrieving_items(self):
     
      entry1 = Users() 
      entry1.Name = 'Ray'      
      entry1.addres = 'brgy.'
      entry1.age = '22.'
      entry1.dswd = '00111'
      entry1.save()   
      entry1 = Item()  
      entry2.Name = 'Ryan'      
      entry2.addres = 'Block o'
      entry2.age = '23'
      entry2.dswd = '5555'
      entry2.save()      
      items = item.object.all()                  
      self.assertEqual(items.count(), 2) 
      items1 = items[0]
      items2 = items[2]      	     
      self.assertEqual(items1.brgyid, '143')
      self.assertEqual(items2.brgyid, '134')



