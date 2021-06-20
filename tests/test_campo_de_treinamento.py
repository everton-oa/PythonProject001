import time
from tests.test_base import BaseTest
from pages.campo_de_treinamento_page import CampoDeTreinamentoPage


class TestCadastro(BaseTest):
    def test_cadastro_com_sucesso(self):
        self.campoDeTreinamento = CampoDeTreinamentoPage(self.driver)
        self.campoDeTreinamento.open_campo_de_treinamento_url()
        self.campoDeTreinamento.fill_name("Everton")
        self.campoDeTreinamento.fill_sobrenome("Araujo")
        self.campoDeTreinamento.select_sexo_feminino()
        self.campoDeTreinamento.select_comida_favorita_carne()
        self.campoDeTreinamento.select_escolaridade_mestrado()
        self.campoDeTreinamento.select_esporte_corrida()
        self.campoDeTreinamento.cadastra()
        time.sleep(1)
