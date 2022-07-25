import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from google_search import driver, google_search, gs_1st_link_click



def javatpoint_all_courses():
    print("getting all courses name..", driver.current_url)
    tt = driver.find_elements("xpath", "//*[@id='city']/table/tbody/tr/td//*/p")
    for i in tt:
        print(i.text)

if __name__ == '__main__':
    google_search('javatpoint')
    gs_1st_link_click()
    javatpoint_all_courses()
    print('driver closing..')
    driver.close()