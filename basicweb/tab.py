import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver"))
driver.get("https://www.bing.com")

lnks = driver.find_elements(By.TAG_NAME, "a")
for i in range(len(lnks)):
    if lnks[i].is_displayed():
        print(lnks[i].text)
        lnks[i].send_keys(Keys.TAB)

time.sleep(5)
driver.quit()