import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver"))
driver.get("https://www.bing.com")
p1 = driver.find_elements(By.TAG_NAME, "a")
for i in range(len(p1)):
    if p1[i].is_displayed():
        print(p1[i].text)
driver.quit()
