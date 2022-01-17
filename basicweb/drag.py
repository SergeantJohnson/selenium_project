import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
driver.get("https://jqueryui.com/draggable/")

driver.maximize_window()

frm = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(frm)

to_be_dragged = driver.find_element(By.ID, "draggable")
print(to_be_dragged.size)
print(to_be_dragged.location)

ActionChains(driver).drag_and_drop_by_offset(to_be_dragged, 150, 100).perform()

time.sleep(2)
driver.quit()
