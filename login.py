'''

Login into website

@author: rfogliat@andrew.cmu.edu

 '''


from ScrapITRA.import_modules import *


def login(username, password, browser):

    browser.find_element_by_class_name('btnconnect').click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn')))

    user_box = browser.find_element_by_xpath('//*[@id="fMemb"]/input[1]')
    user_box.send_keys(username)

    password_box = browser.find_element_by_xpath('//*[@id="fMemb"]/input[2]')
    password_box.send_keys(password)

    browser.find_element_by_class_name('btn').click()


__all__ = ['login']
