from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from selenium import webdriver
import time
import unittest
from pytest import mark


class LoginTests:
    def test_login_valid(self, chrome_browser):
        chrome_browser.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_on_login_button()

        homePage = HomePage(driver)
        homePage.click_on_welcome()
        homePage.click_on_logout()
        time.sleep(2)
