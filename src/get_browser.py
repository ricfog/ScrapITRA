'''

 Get browser

 @author: rfogliat@andrew.cmu.edu

'''

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os




def get_browser(webpage, head=True, path_driver=None):
    options = Options()
    options.headless = head # go headless
    if not path_driver:
        path_driver = 'Drivers/firefox_mac'
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #path_driver = os.path.join(dir_path,'Drivers/firefox_mac')
    browser = webdriver.Firefox(options=options, executable_path=path_driver)

    browser.get(webpage)
    return browser
