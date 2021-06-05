from locators.Locators import Locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_on_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_on_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()