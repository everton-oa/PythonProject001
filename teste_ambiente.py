import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("file://" + os.getcwd() + "/resources/componentes.html")
driver.find_element_by_id("elementosForm:nome").send_keys("Everton")
driver.find_element_by_id("elementosForm:sobrenome").send_keys("Araujo")
driver.find_element_by_id("elementosForm:sexo:0").click()
driver.find_element_by_id("elementosForm:comidaFavorita:0").click()
opcoesEscolaridade = Select(driver.find_element_by_id("elementosForm:escolaridade"))
opcoesEscolaridade.select_by_visible_text("Superior")
opcoesEsporte = Select(driver.find_element_by_id("elementosForm:esportes"))
opcoesEsporte.select_by_visible_text("Futebol")
opcoesEsporte.select_by_visible_text("Corrida")
driver.find_element_by_id("elementosForm:cadastrar").click()
time.sleep(3)
driver.close()
driver.quit()
