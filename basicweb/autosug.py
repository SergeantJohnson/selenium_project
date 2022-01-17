import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
driver.get("https://www.bing.com")

str = "Charula"
txtbx = driver.find_element(By.ID, "sb_form_q")
txtbx.send_keys("Charula")
time.sleep(2)
suggs = driver.find_elements(By.XPATH, "//span[@class='sa_tm_text']")
print(suggs)
for i in range(len(suggs)):
    print(suggs[i].text)

driver.get_screenshot_as_file("C:\\Users\\charu\\workspace_python\\datafiles\\autosug.png")
#txtbx.send_keys(Keys.ENTER)

driver.quit()