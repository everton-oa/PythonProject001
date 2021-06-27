from pages.browser_manager import Browser
from pytest import fixture


@fixture(scope="class", params=[Browser.CHROME])
def init_browser(request):
    web_driver = Browser.create_new_driver(request.param)
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()
