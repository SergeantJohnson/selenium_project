import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\geckodriver.exe"))
#driver.get("https://www.salesforce.com/in/")
driver.get("https://www.w3schools.com/bootstrap/bootstrap_dropdowns.asp")
#driver.get("https://www.google.com")

#login_element = driver.find_elements(By.XPATH, "//a[@href='https://login.salesforce.com/?locale=in']")
#login_element[0].click()
#signup_page = driver.find_element(By.XPATH, "//a[@class='button secondary']")
#signup_page.click()
#roles = driver.find_elements(By.NAME, 'UserFirstName')
roles = driver.find_element(By.XPATH, "//ul[@aria-labelledby = 'menu1']")
print(roles)
ddlist = roles.find_elements(By.TAG_NAME, "a")
print(ddlist)
for i in range(len(ddlist)):
    print(ddlist[i])
    print(ddlist[i].text)
driver.quit()
