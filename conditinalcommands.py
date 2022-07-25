import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\webdrivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/")

user_ele = driver.find_element("name", "userName")
pwd_ele = driver.find_element("name", "password")


user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
sub = driver.find_element("name", "submit")
sub.click()

print("going to logged page...")
#next page

log_success = driver.find_element("xpath", "//h3[text()='Login Successfully']")
if log_success.is_displayed() == True:
    print("find login successfully next finding flights button")
    time.sleep(5)
    flights = driver.find_element("xpath", "//a[text()='Flights']")
    print("find the flights button", flights.is_displayed())
    flights.click()
    print("flights button clicked")
    time.sleep(10)
    roundtrip = driver.find_element("css selector", "input[value=roundtrip]")
    print("Round trip radio button is selected", roundtrip.is_selected())
    oneway = driver.find_element("css selector", "input[value=oneway]")
    print("oneway radio button is selected", oneway.is_selected())

else:
    print("not find login successfully")

driver.quit()
