import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
driver.get("https://www.bing.com/account")
dd = driver.find_element(By.ID, "rpp")

s = Select(dd)
s.select_by_index(2)
p1 = s.options
for p2 in p1:
    print(p2.get_attribute("value"))
time.sleep(5)
driver.quit()
