from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Home.login_page import LoginPage
import os
import unittest

class HomePage(unittest.TestCase):


    def __init__(self):
        self.baseUrl = "https://letskodeit.teachable.com/"
        self.chromeLocation = "G:/Piyush/BrowserBuild/ChromeDriver/ChromeDriver78.0.3904.70/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = self.chromeLocation
        self.driver = webdriver.Chrome(self.chromeLocation)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_validLogin(self):
        self.driver.get(self.baseUrl)
        lp = LoginPage(self.driver)
        lp.login_HomePage("test@email.com", "abcabc")

        actualText = (self.driver.find_element(By.XPATH, "//a[contains(text(), 'My Courses')]")).text
        expectedText = "My Courses"
        if actualText is not None:
            if actualText == expectedText:
                print("User was able to login to account")
            else:
                print("User was not able to login to account")
        else:
            print("User login page not present")

