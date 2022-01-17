import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver"))
driver.get("https://www.bing.com/account")
#driver.find_element(By.XPATH,"//input[@id="newwnd"]")
if not driver.find_element(By.XPATH,"//input[@id='newwnd']").is_selected():
    print("Not selected")
    driver.find_element(By.XPATH, "//input[@id='newwnd']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//input[@id='sv_btn']").click()

driver.get("https://www.bing.com/account")
if not driver.find_element(By.XPATH, "//input[@id='newwnd']").is_selected():
    print("Still not Selected")
else:
    print("Selected")
time.sleep(4)
driver.quit()
