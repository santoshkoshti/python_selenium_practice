from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from google_search import driver, gs_1st_link_click, google_search


def gmail_login(uname, pwd):
    driver.get("https://www.gmail.com")
    driver.find_element("id", "identifierId").send_keys(uname)
    time.sleep(2)
    driver.find_element("xpath", "//*[@id='identifierNext']").click()
    time.sleep(3)
    driver.find_element("name", "password").send_keys(pwd)
    time.sleep(3)
    driver.find_element("xpath", "//span[contains(text(),'Next')][1]").click()
    time.sleep(8)
    driver.save_screenshot("C:\\Users\\SANTOSH KOSHTI\\Desktop\\screenshot.png")
    driver.close()
    print("Gmail login has been successfully completed")

uname = "dummysantoshkk@gmail.com"
pwd = "Santu@1995"
gmail_login(uname,pwd)