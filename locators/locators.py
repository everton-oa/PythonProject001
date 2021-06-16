import os


class Locators:

    # Campo de treinamento locators
    NOME_TEXTFIELD = "elementosForm:nome"
    SOBRENOME_TEXTFIELD = "elementosForm:sobrenome"
    SEXO_RADIO = "elementosForm:sexo:0"
    CADASTRAR_BUTTON = "elementosForm:cadastrar"

    # Campo de treinamento locators
    CAMPO_DE_TREINAMENTO_URL = "file://" + os.getcwd() + "/resources/componentes.html"
