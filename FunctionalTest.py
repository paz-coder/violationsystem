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
		inputname = self.browser.find_element_by_id('Name')
		inputadd = self.browser.find_element_by_id('Address1')
		inputage = self.browser.find_element_by_id('Age1')
		inputdswd = self.browser.find_element_by_id('Dswd1')
		btn_button = self.browser.find_element_by_id('btnf')
		self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
		inpName.click()
		inpName.send_keys('Ray')
		time.sleep(1)
		inpNameF.send_keys('brgy')
		time.sleep(1)
		inpNameL.send_keys('22')
		time.sleep(1)
		inpNameM.send_keys('0110')
		time.sleep(1)
		btn_button.click()
		time.sleep(1)

		def checking_if_in_table_list(self,row_test):
			table = self.browser.find_element_by_id('Table')
			rows = table.find_elements_by_tag_name('tr')
			self.assertIn('Ray', [rows.text for rows in rows])

if __name__ == '__main__':
		unittest.main(warnings='ignore')
