from Pages.CampoDeTreinamentoPage import CampoDeTreinamentoPage
from tests.test_base import BaseTest
from Pages.basePage import BasePage
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class TestCadastro(BaseTest):
    def test_cadastro_com_sucesso(self):
        self.campoDeTreinamento = CampoDeTreinamentoPage(self.driver)
        self.campoDeTreinamento.fill_name("Everton")
        self.campoDeTreinamento.fill_sobrenome("Araujo")
        self.campoDeTreinamento.select_sexo_masculino
        self.campoDeTreinamento.cadastra
        self.time.sleep(3)
