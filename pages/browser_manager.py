from selenium import webdriver


class Browser:

    CHROME = 0
    FIREFOX = 1

    def create_new_driver(driver_id):
        if Browser.CHROME == driver_id:
            print("\nInitiating ChromeDriver")
            driver = webdriver.Chrome()
        elif Browser.FIREFOX == driver_id:
            driver = webdriver.Firefox()
            print("\nInitiating GeckoDriver")
        return driver
