import json

import pytest

from Photographers.api_collections.booking_api import BookingAPI
from Photographers.api_collections.data_classes.booking_data import Booking
from Photographers.api_collections.data_classes.change_data import ChangeData
from Photographers.utilities.config_obl import ConfigObject
from Photographers.utilities.config_reader import ReadConfig
from Photographers.utilities.driver_factory import create_driver_factory


@pytest.fixture(scope='session', autouse=True)
def env():
    with open('./../Configurations/env_1.json') as file:
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


@pytest.fixture()
def create_mock_booking():
    mock_data = BookingAPI().get_booking_by_id(3)
    booking = Booking(**mock_data.json())
    return booking

@pytest.fixture()
def update_mock_booking():
    mock_data2 = BookingAPI().get_booking_by_id(7)
    change_data = ChangeData(**mock_data2.json())
    return change_data

@pytest.fixture()
def generate_token():
    pass
