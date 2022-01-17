import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class salesForce:
    def __init__(self):
        print("Init")


    def start(self):
        self.driver = \
            webdriver.Chrome(
                service=
                Service(r"C:\Users\charu\workspace_python\drivers\chromedriver.exe"))
        self.driver.get("https://login.salesforce.com/")
        self.driver.maximize_window()

    def gotopage(self):
        self.driver.find_element(By.XPATH, "//a[@id='signup_link']").click()
        time.sleep(3)

    def fillpage(self):
        self.driver.find_element(By.NAME, "UserFirstName").send_keys("ABCD")
        self.driver.find_element(By.NAME, "UserLastName").send_keys("MNOP")
        self.driver.find_element(By.NAME, "UserTitle").send_keys("Designation")
        self.driver.find_element(By.NAME, "UserEmail").send_keys("abc@yahoo.com")
        self.driver.find_element(By.NAME, "UserPhone").send_keys("1234123412")
        dd_empnum = self.driver.find_element(By.NAME, "CompanyEmployees")
        dd_empnum.find_element(By.XPATH, "//option[@value='500']").click()
        self.driver.find_element(By.NAME, "CompanyName").send_keys("Com1")
        self.driver.find_element(By.NAME, "CompanyCountry").send_keys("India")
        chkbox = self.driver.find_element(By.CLASS_NAME, "checkbox-ui")
        if not chkbox.is_selected():
            chkbox.click()
        time.sleep(3)

        self.driver.quit()

    def __del__(self):
        pass


# class=checkbox-ui
# #name = "start my free trial"
