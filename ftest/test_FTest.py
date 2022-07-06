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
				table = self.browser.find_element_by_id('studentinfo')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time()-start_time>cWait:
					raise e
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get(self.live_server_url)
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
		self.browser.find_element_by_id('btn').click()
		#time.sleep(1)
		self.checking_if_in_table_list('1: Paz, Eldren TUPC-18-0696 4B Cheating')
		viewlist_url_2 = self.browser.current_url
		pageBody = self.browser.find_element_by_tag_name('body').text

	def test_start_list_and_retrieve_it_2(self):
		self.browser.get(self.live_server_url)
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
		Name.send_keys('Ryan, Balota')
		time.sleep(1)
		Snum.send_keys('TUPC-18-0623')
		time.sleep(1)
		Section.send_keys('4B')
		time.sleep(1)
		Violation.send_keys('Noisy')
		time.sleep(1)
		btn_button.click()
		time.sleep(1)
		self.browser.find_element_by_id('btn').click()
		#time.sleep(1)
		self.checking_if_in_table_list('1: Paz, Eldren TUPC-18-0696 4B Cheating')
		self.checking_if_in_table_list('2: Ryan, Balota TUPC-18-0623 4B Noisy')


