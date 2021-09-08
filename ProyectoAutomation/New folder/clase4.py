from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')

driver.find_element_by_id('search_query_top').send_keys('hola mundo')

driver.find_element_by_name('submit_search').click()
time.sleep(5)

tc.assertEqual('No results were found for your search "hola mundo"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)

driver.find_element_by_link_text('Women').click()
time.sleep(3)

driver.find_element_by_partial_link_text('Dres').click()
time.sleep(3)

driver.find_element_by_link_text('Casual Dresses').click()

#si no se todo el text puedo ponerlo parcial
driver.find_element_by_partial_link_text('Casual').click()

#por class name
driver.find_elements_by_class_name('subcategory-name').click()

#por css
driver.find_elements_by_css_selector('a.subcategory-name').click()

#por xpath
driver.find_element_by_xpath('//*[@id="subcategories"]/ul/li[1]/h5/a').click()

driver.close()
driver.quit()