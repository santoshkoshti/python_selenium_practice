from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.expedia.com/")
# driver.find_element("xpath", "//*[@id='wizardMainRegionV2']/div/div/div/div/ul/li[2]/a/span").click()
driver.find_element(By.XPATH, "//*[@id='wizardMainRegionV2']/div/div/div/div/ul/li[2]/a/span").click()
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[1]/div[2]/button").click()
time.sleep(2)
driver.find_element(By.ID, "location-field-leg1-origin").send_keys("SFO", Keys.ENTER)   #orgin
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='location-field-leg1-destination-menu']/div[1]/div[2]/button").click()
time.sleep(2)
driver.find_element(By.ID, "location-field-leg1-destination").send_keys("NYC", Keys.ENTER)    #destination
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='d1-btn']").click()
driver.find_element(By.ID, "").send_keys("15/07/2022")

driver.find_element(By.ID, "").clear()
driver.find_element(By.ID, "").send_keys("20/07/2022")

driver.find_element(By.XPATH, "").click()

time.sleep(30)
driver.close()