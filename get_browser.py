'''

 Get browser

 @author: rfogliat@andrew.cmu.edu

'''

from ScrapITRA.import_modules import *


def get_browser(webpage):
    options = Options()
    options.headless = True # go headless
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path_driver = os.path.join(dir_path,'Drivers/firefox_mac')
    browser = webdriver.Firefox(options=options, executable_path=path_driver)

    browser.get(webpage)
    return browser
