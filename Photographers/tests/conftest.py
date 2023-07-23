import json

import pytest

from Photographers.api_collections.booking_api import BookingAPI
from Photographers.api_collections.data_classes.booking_data import Booking
from Photographers.utilities.config_reader import ReadConfig
from Photographers.utilities.driver_factory import create_driver_factory


#@pytest.fixture(scope='session', autouse=True)
#def env(request):
#    with open('./../Configurations/env_1.json') as file:
#        f_data = file.read()
#    json_data = json.loads(f_data)
#    return ReadConfig(**json_data)


@pytest.fixture()
def create_driver():
    driver = create_driver_factory(ReadConfig.get_browser_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def create_mock_booking():
    mock_data = BookingAPI().get_booking_by_id(1)
    booking = Booking(**mock_data.json())
    return booking
