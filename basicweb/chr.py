import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver"))
driver.get("https://www.bing.com")
time.sleep(5)
driver.quit()
