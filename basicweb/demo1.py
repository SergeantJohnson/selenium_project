from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class chrome_webdriver_windows:
    def starttest(self):
        driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
        driver.get("https://www.bing.com/")

        driver.find_element(By.ID, "sb_form_q").send_keys("ABCD")
        driver.find_element(By.XPATH, "//label[@for='sb_form_go']").click()

        time.sleep(2)
        driver.quit()


cw = chrome_webdriver_windows()
cw.starttest()