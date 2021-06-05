from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from selenium import webdriver
import time
import unittest
from pytest import mark


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @mark.login
    @mark.smoke
    def test_login_valid(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_on_login_button()

        homePage = HomePage(driver)
        homePage.click_on_welcome()
        homePage.click_on_logout()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
