import json

import pytest
from selenium.webdriver import Chrome, ActionChains, Keys
from selenium import webdriver

from Photographers.utilities.config_objects import ConfigObject
from Photographers.utilities.config_reader import ReadConfig
from Photographers.utilities.driver_factory import create_driver_factory


def pytest_adoption(parser):
    parser.addoption('--env', action='store', help='specify env name', required= True)


@pytest.fixture(scope='session', autouse=True)
def env(request):
    env_name = request.config.getoption('--env')
    with open(f'./../Configurations/{env_name}.json') as file:
        f_data = file.read()
    json_data = json.loads(f_data)
    return ConfigObject(**json_data)


@pytest.fixture()
def create_driver():
    driver = create_driver_factory(ReadConfig.get_browser_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()

