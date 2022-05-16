from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
from selenium.webdriver.support.ui import Select
from django.test import LiveServerTestCase

cWait = 3
class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def checking_if_in_table_list(self,row_text):
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(0.2)
			try:
				table = self.browser.find_element_by_id(' member')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time()-start_time>cWait:
					raise e
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get(self.live_server_url)
		self.assertIn('4PS MONITORING SYSTEM', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Member Form', headerText)
		Name = self.browser.find_element_by_id('Name')
		Add = self.browser.find_element_by_id('address')
		Ag = self.browser.find_element_by_id('age')
		Ds = self.browser.find_element_by_id('dswd')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(Name.get_attribute('placeholder'),'Enter your name here.')
		Name.click()
		Name.send_keys('juan j')
		time.sleep(1)
		Add.send_keys('san antonio')
		time.sleep(1)
		Ag.send_keys('40')
		time.sleep(1)
		Ds.send_keys('0011')
		time.sleep(1)
		btn_button.click()
		time.sleep(1)
		self.browser.find_element_by_id('btn').click()
		#time.sleep(1)
		self.checking_if_in_table_list('1: juan j')
		viewlist_url_2 = self.browser.current_url
		pageBody = self.browser.find_element_by_tag_name('body').text

	def test_start_list_and_retrieve_it_2(self):
		self.browser.get(self.live_server_url)
		self.assertIn('4PS MONITORING SYSTEM', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Member Form', headerText)
		Name = self.browser.find_element_by_id('Name')
		Add = self.browser.find_element_by_id('address')
		Ag = self.browser.find_element_by_id('age')
		Ds = self.browser.find_element_by_id('dswd')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(Name.get_attribute('placeholder'),'Enter your name here.')
		Name.click()
		Name.send_keys('juan j')
		time.sleep(1)
		Add.send_keys('san antonio')
		time.sleep(1)
		Ag.send_keys('40')
		time.sleep(1)
		Ds.send_keys('0011')
		time.sleep(1)
		btn_button.click()


		self.assertIn('4PS MONITORING SYSTEM', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Member Form', headerText)
		Name = self.browser.find_element_by_id('Name')
		Add = self.browser.find_element_by_id('address')
		Ag = self.browser.find_element_by_id('age')
		Ds = self.browser.find_element_by_id('dswd')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(Name.get_attribute('placeholder'),'Enter your name here.')
		Name.click()
		Name.send_keys('john b')
		time.sleep(1)
		Add.send_keys('san carlos')
		time.sleep(1)
		Ag.send_keys('30')
		time.sleep(1)
		Ds.send_keys('0022')
		time.sleep(1)
		btn_button.click()
		time.sleep(1)
		self.browser.find_element_by_id('btn').click()
		#time.sleep(1)
		self.checking_if_in_table_list('1: juan j san antonio 40 0011')
		self.checking_if_in_table_list('2: john b san carlos 30 0022')

'''from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('4PS MONITORING SYSTEM', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Member Form', headerText)
		inputName = self.browser.find_element_by_id('Name')
		inputadd = self.browser.find_element_by_id('address')
		inputage = self.browser.find_element_by_id('age')
		inputdswd = self.browser.find_element_by_id('dswd')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(inputName.get_attribute('placeholder'),'Enter your name here.')
		inputName.click()
		inputName.send_keys('Ray')
		time.sleep(2)
		inputadd.send_keys('bgry.')
		time.sleep(2)
		inputage.send_keys('22')
		time.sleep(2)
		inputdswd.send_keys('00111')
		time.sleep(2)
		btn_button.click()
		time.sleep(2)

		inputName = self.browser.find_element_by_id('Name')
		inputadd = self.browser.find_element_by_id('address')
		inputage = self.browser.find_element_by_id('age')
		inputdswd = self.browser.find_element_by_id('dswd')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(inputName.get_attribute('placeholder'),'Enter your name here.')
		inputName.click()
		inputName.send_keys('Ryan')
		time.sleep(2)
		inputadd.send_keys('Block o')
		time.sleep(2)
		inputage.send_keys('23')
		time.sleep(2)
		inputdswd.send_keys('5555')
		time.sleep(2)
		btn_button.click()
		time.sleep(2)



	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_id('Table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('Ray', [rows.text for rows in rows])

if __name__ == '__main__':
	unittest.main(warnings='ignore')'''



  
      
