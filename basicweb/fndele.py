from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\geckodriver.exe"))
driver.get("https://www.bing.com")
p1 = driver.find_elements(By.TAG_NAME, "a")
print(p1)
driver.quit()
