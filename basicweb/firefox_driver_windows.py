from selenium import webdriver
from selenium.webdriver.firefox.service import Service


class Runfftests:
    def __init__(self):
        pass

    def startfftests(self):
        driver = webdriver.Firefox(service=Service("C:\\Users\\charu\\workspace_python\\drivers\\geckodriver.exe"))
        driver.get("https://courses.letskodeit.com/practice")


ff = Runfftests()
ff.startfftests()

