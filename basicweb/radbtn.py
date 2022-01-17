import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
driver.get("https://www.bing.com/account")
driver.find_element(By.XPATH, "//input[@id='adlt_set_strict']").click()
time.sleep(5)
driver.quit()