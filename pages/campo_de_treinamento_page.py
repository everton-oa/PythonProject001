import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CampoDeTreinamentoPage(BasePage):

    NOME_TEXTFIELD = (By.ID, "elementosForm:nome")
    SOBRENOME_TEXTFIELD = (By.ID, "elementosForm:sobrenome")
    SEXO_RADIO = (By.ID, "elementosForm:sexo:0")
    CADASTRAR_BUTTON = (By.ID, "elementosForm:cadastrar")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("file://" + os.getcwd() + "/resources/componentes.html")

    def fill_name(self, name):
        self.send_key(self.NOME_TEXTFIELD, name)

    def fill_sobrenome(self, sobrenome):
        self.send_key(self.SOBRENOME_TEXTFIELD, sobrenome)

    def select_sexo_masculino(self):
        self.click(self, self.SEXO_RADIO)

    def cadastra(self):
        self.click(self.CADASTRAR_BUTTON)
