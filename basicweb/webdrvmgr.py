import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://www.bing.com")
time.sleep(2)
driver.quit()
