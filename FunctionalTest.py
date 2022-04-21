import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

class PageTest(unittest.TestCase):
	def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('id_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
      	               raise e                  
                   time.sleep(0.5)  

                   def setUp(self):
                   	self.browser = webdriver.Firefox()
                   	def test_browser_title(self):
                   		self.browser.get('http://localhost:8000/')
                   		#self.browser.get(self.live_server_url)
                   		self.assertIn('MEMBER FORM',self.browser.title)
                   		header_text = self.browser.find_element_by_tag_name('h1').text
                   		self.assertIn('MEMBER FORM', header_text)
	 
	 
	 
	
	inputmember = self.browser.find_element_by_id('member')
	self.assertEqual(inputmember.get_attribute('placeholder'),'Enter your Fullname')
	inputmember.click()
	time.sleep(1)
	inputmember.send_keys('Leonalyn Maglines')
	time.sleep(1)
	 
	inputaddress = self.browser.find_element_by_id('address')
    self.assertEqual(inputaddress.get_attribute('placeholder'),'Enter your Address')
    inputaddress.click()
    time.sleep(1)
    inputaddress.send_keys('Brgy padios')
    time.sleep(1)
	 
	inputage = self.browser.find_element_by_id('age')
	self.assertEqual(inputage.get_attribute('placeholder'),'Enter your Age')
	inputage.click()
	time.sleep(1)
	inputage.send_keys('22 yrs. old')
	time.sleep(1)
	 
	
    inputdswd = self.browser.find_element_by_id('dswd')
    self.assertEqual(inputdswd.get_attribute('placeholder'),'ID Number')
    inputdswd.click()
    time.sleep(1)
    inputdswd.send_keys('0000111')
    time.sleep(1)
	 
	 
    inputphone = self.browser.find_element_by_id('cellphone')
    self.assertEqual(inputphone.get_attribute('placeholder'),'Cellphone Number')
    inputphone.click()
    time.sleep(1)
    inputphone.send_keys('09095567845')
    time.sleep(1)

    inputday = self.browser.find_element_by_id('member')
    self.assertEqual(inputday.get_attribute('placeholder'),'How many')
    inputphone.click()
    time.sleep(1)
    inputphone.send_keys('3')
    time.sleep(1)
	 
    btnContinue = self.browser.find_element_by_id('btnF')
    btnContinue.cl
