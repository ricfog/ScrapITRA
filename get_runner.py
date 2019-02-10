'''

get list of available runners

@author: rfogliat@andrew.cmu.edu

'''


from import_modules import *



def get_runner(browser, first_name=None, last_name=None, nationality=None):

    if first_name==None and last_name==None:
        sys.exit('At least one parameter needs to be specified!')

    else:
        # input information
        if first_name:
            first_name_box = browser.find_element_by_xpath('//*[@id="searchRunner"]/div[1]/form/div[1]/input')
            first_name_box.send_keys(first_name)

        if last_name:
            last_name_box = browser.find_element_by_xpath('//*[@id="searchRunner"]/div[1]/form/div[2]/input')
            last_name_box.send_keys(last_name)

        if nationality:
            el = browser.find_element_by_id('nat')
            for option in el.find_elements_by_tag_name('option'):
                if option.text == nationality:
                    option.click()
                    break



    # retrieve list
    browser.find_element_by_xpath('//*[@id="searchRunner"]/div[1]/form/a').click()
    WebDriverWait(browser, 100).until(EC.visibility_of_element_located((By.ID, 'searchRes')))


    elements = browser.find_element_by_id('searchRes').find_elements_by_class_name('fc')

    list_runners = []
    for element in elements:
        list_runners.append(element.get_attribute('data-url'))

    return list_runners
