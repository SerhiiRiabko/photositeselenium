import pytest
from selenium.webdriver import Chrome, ActionChains, Keys
from selenium import webdriver
from Selenium_for_site.utilities.config_reader import ReadConfig
from Selenium_for_site.utilities.driver_factory import create_driver_factory


@pytest.fixture()
def create_driver():
    driver = create_driver_factory(ReadConfig.get_browser_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()
