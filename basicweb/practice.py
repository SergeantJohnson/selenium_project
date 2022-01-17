from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class ffDriversWindows:
    def starttest(self):
        driver = webdriver.Firefox(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\geckodriver.exe"))
        driver.get("https://courses.letskodeit.com/practice")


class chromeDriversWindows:
    def starttest(self):
        driver = webdriver.Chrome(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\chromedriver.exe"))
        driver.get("https://courses.letskodeit.com/practice")
        elementbyid=driver.find_element(By.ID, "name")
        print(elementbyid)

#ff = ffDriversWindows()
#ff.starttest()

ch = chromeDriversWindows()
ch.starttest()

