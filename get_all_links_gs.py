import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from google_search import google_search, driver

google_search("javatpoint")
lists = []

pageno = 1
def all_links():
    print("getting page no", pageno)
    lnks = driver.find_elements(By.TAG_NAME, "a")
    for lnk in lnks:
        link = lnk.get_attribute('href')
        lists.append(link)


def next_page_click_gs():
    for check in range(1, 100):
        all_links()
        time.sleep(3)
        try:
            driver.find_element("xpath", "//*[@id='pnnext']/span[2]").click()
        except:
            print("it is last page there is no next page..")
            break;

if __name__ == '__main__':
    all_links()
    next_page_click_gs()
    print(lists)
    driver.close()
    print("sample test case successfully completed")
