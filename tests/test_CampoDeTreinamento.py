import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class TestCadastro:
    def test_cadastro_com_sucesso(self, driver):
        self.driver.find_element_by_id("elementosForm:nome").send_keys("Everton")
        self.driver.find_element_by_id("elementosForm:sobrenome").send_keys("Araujo")
        self.driver.find_element_by_id("elementosForm:sexo:0").click()
        self.driver.find_element_by_id("elementosForm:comidaFavorita:0").click()
        opcoesEscolaridade = Select(
            self.driver.find_element_by_id("elementosForm:escolaridade")
        )
        opcoesEscolaridade.select_by_visible_text("Superior")
        opcoesEsporte = Select(self.driver.find_element_by_id("elementosForm:esportes"))
        opcoesEsporte.select_by_visible_text("Futebol")
        opcoesEsporte.select_by_visible_text("Corrida")
        self.driver.find_element_by_id("elementosForm:cadastrar").click()
        self.time.sleep(3)
