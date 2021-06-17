import os
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("file://" + os.getcwd() + "/resources/componentes.html")
import pdb

pdb.set_trace()
print(driver.current_url)
driver.find_element_by_id("")
driver.quit()
