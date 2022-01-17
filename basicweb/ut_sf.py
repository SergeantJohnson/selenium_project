# from sf import salesForce
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import time


class ut(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # cls.driver = \
        #    webdriver.Chrome(
        #        service=
        #        Service(r"C:\Users\charu\workspace_python\drivers\chromedriver.exe"))
        cls.driver.get("https://login.salesforce.com/")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")
        cls.driver.quit()

    def test_a_gotopage(self):
        self.driver.find_element(By.XPATH, "//a[@id='signup_link']").click()
        time.sleep(3)

    def test_b_fillpage(self):
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


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=r"C:\Users\charu\workspace_python\selenium_project\reports"))
