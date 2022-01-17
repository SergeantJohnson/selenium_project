import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service = Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
driver.get("https://www.w3schools.com/tags/")
driver.maximize_window()

for _ in range(2,5,1):
    print(driver.find_element(By.XPATH, "//tr["+str(_)+"]/td[1]").text)
    print(driver.find_element(By.XPATH, "//tr["+str(_)+"]/td[2]").text)

time.sleep(2)
driver.quit()