from locators.locators import CampoDeTreinamento
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os


class CampoDeTreinamentoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.NOME_TEXTFIELD = (By.ID, CampoDeTreinamento.NOME_TEXTFIELD)
        self.SOBRENOME_TEXTFIELD = (By.ID, CampoDeTreinamento.SOBRENOME_TEXTFIELD)
        self.SEXO_MASCULINO_RADIO = (By.ID, CampoDeTreinamento.SEXO_MASCULINO_RADIO)
        self.SEXO_FEMININO_RADIO = (By.ID, CampoDeTreinamento.SEXO_FEMININO_RADIO)
        self.COMIDA_FAVORITA_CARNE = (By.ID, CampoDeTreinamento.COMIDA_FAVORITA_CARNE)
        self.COMIDA_FAVORITA_VEGETARIANO = (
            By.ID,
            CampoDeTreinamento.COMIDA_FAVORITA_VEGETARIANO,
        )
        self.SELECT_ESCOLARIDADE = (By.ID, CampoDeTreinamento.SELECT_ESCOLARIDADE)
        self.SELECT_ESPORTE = (By.ID, CampoDeTreinamento.SELECT_ESPORTE)
        self.CADASTRAR_BUTTON = (By.ID, CampoDeTreinamento.CADASTRAR_BUTTON)
        self.RESULTADO_CADASTRO = (By.ID, CampoDeTreinamento.RESULTADO_CADASTRO)

    def open_campo_de_treinamento_url(self):
        self.open_url("file://" + os.getcwd() + "/resources/componentes.html")

    def fill_name(self, name):
        self.send_keys(self.NOME_TEXTFIELD, name)

    def fill_sobrenome(self, sobrenome):
        self.send_keys(self.SOBRENOME_TEXTFIELD, sobrenome)

    def select_sexo_masculino(self):
        self.click_radio(self.SEXO_MASCULINO_RADIO)

    def select_sexo_feminino(self):
        self.click_radio(self.SEXO_FEMININO_RADIO)

    def select_comida_favorita_carne(self):
        self.click_checkbox(self.COMIDA_FAVORITA_CARNE)

    def select_comida_favorita_vegetariano(self):
        self.click_checkbox(self.COMIDA_FAVORITA_VEGETARIANO)

    def select_escolaridade_mestrado(self):
        self.select(self.SELECT_ESCOLARIDADE, "Mestrado")

    def select_esporte_corrida(self):
        self.select(self.SELECT_ESPORTE, "Corrida")

    def cadastra(self):
        self.click(self.CADASTRAR_BUTTON)

    def resultado_cadastro(self):
        return self.get_element_text(self.RESULTADO_CADASTRO)
