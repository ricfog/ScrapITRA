import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


from get_runner import *
from scrap_record import *


options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path='/Users/franco.fogliato/Desktop/chromedriver', chrome_options=options)

#browser = webdriver.Chrome(executable_path='/Users/franco.fogliato/Desktop/chromedriver')
browser.get('https://itra.run/community/')

webpage_list = get_runner(last_name='Fogliato', browser=browser)
l = []
for webpage in webpage_list:
    l.append(webpage)
    l.append(scrap_record(webpage, browser))
print(l)
browser.quit()
