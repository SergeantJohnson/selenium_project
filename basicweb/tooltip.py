import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
driver.get("https://jqueryui.com/tooltip/")
driver.maximize_window()

frm = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(frm)

#resiz = driver.find_element(By.ID, "resizable")
src= driver.find_element(By.ID, 'age')
tt = src.get_attribute("title")
print(tt)

driver.quit()