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
		inputName = self.browser.find_element_by_id('Name')
		inputadd = self.browser.find_element_by_id('address')
		inputage = self.browser.find_element_by_id('age')
		inputdswd = self.browser.find_element_by_id('dswd')
		inputmem = self.browser.find_element_by_id('member')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(inputName.get_attribute('placeholder'),'Enter your name here.')
		inputName.click()
		inputName.send_keys('Ray')
		time.sleep(1)
		inputadd.send_keys('bgry.')
		time.sleep(1)
		inputage.send_keys('22')
		time.sleep(1)
		inputdswd.send_keys('00111')
		time.sleep(1)
		btn_button.click()
		time.sleep(1)
		inputmem.send_keys('3')
		time.sleep(1)
		btn_button.click()
		time.sleep(1)

	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_id('Table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('Ray', [rows.text for rows in rows])

if __name__ == '__main__':
	unittest.main(warnings='ignore')
