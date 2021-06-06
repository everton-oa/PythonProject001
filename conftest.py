from pytest import fixture
from selenium import webdriver


@fixture(scope="class")
def init_browser(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = webdriver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()
