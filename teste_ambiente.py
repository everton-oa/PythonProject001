import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("file://" + os.getcwd() + "/resources/componentes.html")
driver.quit()
