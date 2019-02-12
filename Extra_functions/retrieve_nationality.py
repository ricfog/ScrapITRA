'''
Retrieve list of available nationalities

@author: rfogliat@andrew.cmu.edu

'''

from import_modules import *


def retrieve_nat(webpage, browser=None):


    el = browser.find_element_by_id('nat')
    list_nat = []
    for option in el.find_elements_by_tag_name('option')[1:]:
        list_nat.append(option.text)

    return list_nat
