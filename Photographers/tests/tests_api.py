import requests
from http import HTTPStatus

from Photographers.api_collections.booking_api import BookingAPI
from Photographers.tests.conftest import create_mock_booking


# from Photographers.tests.conftest import create_mock_booking


def test_status_code_200_ajax():
    response = requests.get('https://reqres.in/api/users?page=2')
    response_data = response.json()
    assert response.status_code == HTTPStatus.OK, "Code is not 200"
    assert response_data['page'] == 2, "Not 2d page is opened"
    assert response_data['total'] == 12, "Numbers of page is not 12"


def test_status_code_200_booking():
    booking_api = BookingAPI()
    response = booking_api.get_booking_by_id(booking_id=1)
    booking = response.json()
    assert response.status_code == HTTPStatus.OK, "Code is not 200"
    # assert response_data['firstname'] == 'Jim', "Name is not as in DB"
    # assert response_data['lastname'] == 'Brown', "LName is not as in DB"
    # assert response_data['totalprice'] == 496, "Total price is incorrect"
    # assert response_data['depositpaid'] is True, "Deposit is not True"
    assert booking['firstname'] == 'Mark', "Name is not as in DB"
    assert booking['lastname'] == 'Brown', "LName is not as in DB"
    assert booking['totalprice'] == 157, "Total price is incorrect"
    assert booking['depositpaid'] is False, "Deposit is not True"


def test_create_booking():
    booking_api = BookingAPI()

    response = booking_api.create_booking(create_mock_booking)
    c = 0
