from pytest import fixture
from selenium import webdriver


@fixture(scope="class")
def init_browser(request):
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()
