import os
from selenium import webdriver

driver = webdriver.Chrome()
print(os.getcwd())
driver.get("file://" + os.getcwd() + "/resources/componentes.html")
driver.find_element_by_id("elementosForm:nome").send_keys("testes")
# driver.quit()
