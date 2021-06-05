from locators.Locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_typebox_id = Locators.username_typebox_id
        self.password_typebox_id = Locators.password_typebox_id
        self.login_button_id = Locators.login_button_id

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_typebox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_typebox_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()
