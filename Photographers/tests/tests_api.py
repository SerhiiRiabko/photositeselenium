import json
import requests
from http import HTTPStatus
from Photographers.api_collections.booking_api import BookingAPI
from Photographers.tests.conftest import create_mock_booking


def test_status_code_200_ajax():
    response = requests.get('https://reqres.in/api/users?page=2')
    response_data = response.json()
    assert response.status_code == HTTPStatus.OK, "Code is not 200"
    assert response_data['page'] == 2, "Not 2nd page is opened"
    assert response_data['total'] == 12, "Numbers of pages is not 12"


def test_status_code_200_booking():
    booking_api = BookingAPI()
    response = booking_api.get_booking_by_id(booking_id=3)
    booking = response.json()
    assert response.status_code == HTTPStatus.OK, "Code is not 200"
    assert booking['firstname'] == 'Sally', "Name is not as in DB"
    assert booking['lastname'] == 'Ericsson', "LName is not as in DB"
    assert booking['totalprice'] == 158, "Total price is incorrect"
    assert booking['depositpaid'] is False, "Deposit is not True"


def test_create_booking(create_mock_booking):
    booking_api = BookingAPI()
    booking_obj = create_mock_booking
    response = booking_api.create_booking(booking_obj)
    value = response.json()
    booking_id = value['bookingid']
    response2 = booking_api.get_booking_by_id(booking_id=booking_id)
    booking = response2.json()
    assert response.status_code == 200, "Code is not 200"
    assert booking == value['booking']


def test_update_booking(update_mock_booking):
    booking_api = BookingAPI()
    booking_obj = update_mock_booking
    response = booking_api.update_booking_by_id(booking_id=45, body=booking_obj,
                                                headers={'Content-Type': 'application/json',
                                                         'Accept': 'application/json',
                                                         'Authorization': 'token=abc123'})
    value = response.json()
    booking_id = value['bookingid']
    response2 = booking_api.get_booking_by_id(booking_id=booking_id)
    value_update = response2.json()

    assert response.status_code == 200, "Code is not 200"
    assert value_update == value, 'Changes are not applied'


