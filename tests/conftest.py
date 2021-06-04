import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
