from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from utilities.config_reader import get_headless_status


CHROME = 1
FIREFOX = 2


def create_driver_factory(driver_id):
    if int(driver_id) == CHROME:
        chrome_options = Options()
        driver = webdriver.Chrome()

        chrome_options.add.argument('--headless')
        chrome_options.add.argument('--no-sandbox')
        return Chrome(service=chrome_service(ChromeDriverManager().install()), options=chrome_options)
        
        return driver
    elif int(driver_id) == FIREFOX:
        driver = webdriver.Firefox()
        return driver
    else:
        driver = webdriver.Chrome()
        return driver
