from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Student Violation System', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Student Information', headerText)
		Name = self.browser.find_element_by_id('studentName')
		Snum = self.browser.find_element_by_id('snum')
		Section = self.browser.find_element_by_id('section')
		Violation = self.browser.find_element_by_id('violation')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(Name.get_attribute('placeholder'),'Enter your name here.')
		Name.click()
		Name.send_keys('Paz, Eldren')
		time.sleep(1)
		Snum.send_keys('TUPC-18-0696')
		time.sleep(1)
		Section.send_keys('4B')
		time.sleep(1)
		Violation.send_keys('Cheating')
		time.sleep(1)
		btn_button.click()
		time.sleep(1)

	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_id('studentinfo')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Paz', [rows.text for rows in rows])

if __name__ == '__main__':
	unittest.main(warnings='ignore')