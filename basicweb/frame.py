import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

frm = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(frm)

datebox = driver.find_element(By.ID, "datepicker")
datebox.send_keys("11/08/1976")
datebox.send_keys(Keys.ENTER)
driver.switch_to.default_content()
time.sleep(2)
driver.quit()