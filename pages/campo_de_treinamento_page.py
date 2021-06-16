from locators.locators import Locators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CampoDeTreinamentoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.NOME_TEXTFIELD = (By.ID, Locators.NOME_TEXTFIELD)
        self.SOBRENOME_TEXTFIELD = (By.ID, Locators.SOBRENOME_TEXTFIELD)
        self.SEXO_RADIO = (By.ID, Locators.SEXO_RADIO)
        self.CADASTRAR_BUTTON = (By.ID, Locators.CADASTRAR_BUTTON)

    def open_campo_de_treinamento_url(self):
        self.open_url(Locators.CAMPO_DE_TREINAMENTO_URL)

    def fill_name(self, name):
        self.send_key(self.NOME_TEXTFIELD, name)

    def fill_sobrenome(self, sobrenome):
        self.send_key(self.SOBRENOME_TEXTFIELD, sobrenome)

    def select_sexo_masculino(self):
        self.click(self.SEXO_RADIO)

    def cadastra(self):
        self.click(self.CADASTRAR_BUTTON)
