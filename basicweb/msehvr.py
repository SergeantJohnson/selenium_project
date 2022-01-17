import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
driver.get("https://www.emirates.com/in/english/")
driver.maximize_window()
time.sleep(2)
cookieaccept = driver.find_elements(By.ID, "onetrust-accept-btn-handler")
for i in range(len(cookieaccept)):
    cookieaccept[i].click()

driver.find_element(By.XPATH,"//a[@data-link='MANAGE']").click()
obj = driver.find_element(By.XPATH, "//a[@data-link='MANAGE:Before you fly']")
ActionChains(driver).move_to_element(obj).perform()
#driver.find_element(By.XPATH, "//a[@data-link='MANAGE:Before you fly:Before you fly:Travel information']").click()
val = driver.find_elements(By.XPATH, "(//div[@class='mobile-heading-content-holder' and @role='heading']/span)")
for elem in range(len(val)):
    print("-----", val[elem].text)

#txtbx.send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()