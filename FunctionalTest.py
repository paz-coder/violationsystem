# from selenium import webdriver
# import unittest

# class PageTest(unittest.TestCase):
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()
# 	#def tearDown(self):
# 		#self.browser.quit()
# 	def test_browser_title(self):
# 		self.browser.get('http://localhost:8000')
# 		self.assertIn('Philikula',self.browser.title)
# 		#self.fail('Finish the test!')
# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')

from selenium import webdriver
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
		inpname = self.browser.find_element_by_id('Name')
		btn_Pindot_button = self.browser.find_element_by_id('btnf')

		self.assertEqual(inpname.get_attribute('placeholder'),'Enter your Full Name.')
		inpname.click()
		inpname.send_keys('rayray')
		time.sleep(1)
		btn_Pindot_button.click()
		time.sleep(1)
		
		inpname = self.browser.find_element_by_id('add')
		btn_add_button = self.browser.find_element_by_id('btna')
		self.assertEqual(inputaddress.get_attribute('placeholder'),'Enter your Address.')
		inputaddress = self.browser.find_element_by_id('address')
		inputaddress.click()
		inputaddress.send_keys('Blk 13 lot 10 brgy Dimawari')
		time.sleep(1)
		btn_Pindot_button.click()
		time.sleep(1)

	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_id('registryTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('rayray', [rows.text for rows in rows])

	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_id('registryTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('address', [rows.text for rows in rows])

if __name__ == '__main__':
	unittest.main(warnings='ignore')