import os
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("file://" + os.getcwd() + "/resources/componentes.html")
driver.quit()
