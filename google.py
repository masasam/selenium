#!/usr/bin/python3
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
# headless mode on
options.add_argument('--headless')
options.add_argument('--window-size=1280,1024')
# Chrome webdriver
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.google.co.jp/')

assert 'Google' in driver.title

input_element = driver.find_element_by_name('q')
input_element.send_keys('emacs')
input_element.send_keys(Keys.RETURN)

time.sleep(2)

assert 'emacs' in driver.title

# screenshot
driver.save_screenshot('search_results.png')

for a in driver.find_elements_by_css_selector('h3 > a'):
    print(a.text)
    print(a.get_attribute('href'))

driver.quit()
