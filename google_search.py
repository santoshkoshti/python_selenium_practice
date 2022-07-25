import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os


driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()

def google_search(gsdata):
    driver.get("https://www.google.com/")
    driver.find_element("name", "q").send_keys(gsdata)
    time.sleep(3)
    driver.find_element("name", "btnK").send_keys(Keys.ENTER)
    time.sleep(5)
    print("hi google searching ", gsdata)

def gs_1st_link_click():
    print("clicked on searched results 1st link")
    driver.find_element('xpath', '//*/h3').click()