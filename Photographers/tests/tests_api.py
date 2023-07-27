import json

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
    response = booking_api.get_booking_by_id(booking_id=187)
    booking = response.json()
    assert response.status_code == HTTPStatus.OK, "Code is not 200"
    assert booking['firstname'] == 'Mary', "Name is not as in DB"
    assert booking['lastname'] == 'Jones', "LName is not as in DB"
    assert booking['totalprice'] == 300, "Total price is incorrect"
    assert booking['depositpaid'] is True, "Deposit is not True"


def test_create_booking(create_mock_booking):
    booking_api = BookingAPI()
    booking_obj = create_mock_booking
    response = booking_api.create_booking(booking_obj)
    value = response.json()
    booking_id = value['bookingid']
    response2 = booking_api.get_booking_by_id(booking_id=booking_id)
    booking = response2.json()
    assert response.status_code == 200, "Code is not 200"
    assert booking == value['booking'] # checking all rows that commented later


def test_update_booking(update_mock_booking):
    booking_api = BookingAPI()
    booking_obj = update_mock_booking
    response = booking_api.update_booking_by_id(booking_id=45, body=booking_obj, headers={'Content-Type':
                                                                                             'application/json',
                                                                                         'Accept': 'application/json',
                                                                                         'Authorization': 'token=abc123'})
    value = response.json()
    booking_id = value['bookingid']
    response2 = booking_api.get_booking_by_id(booking_id=booking_id)
    value_update = response2.json()

    assert response.status_code == 200, "Code is not 200"
    assert value_update == value, 'Changes are not applied'


# def test_partial_update_booking(create_mock_booking):
#     booking_api = BookingAPI()
#     booking_obj = create_mock_booking
#     # Create the booking and get the booking ID
#     response = requests.post(BASE_URL + "/booking", json=booking_obj)
#     value = response.json()
#     booking_id = value['bookingid']
#
#     # Partial update the booking with only the fields you want to change
#     partial_update_obj = {
#         "firstname": "Jane",  # Update the firstname
#         # Add other fields you want to update
#     }
#     response = requests.patch(BASE_URL + f"/booking/{booking_id}", json=partial_update_obj)
#
#     # Verify the response status code
#     assert response.status_code == 200, "Code is not 200"
#
#     # Get the updated booking and check if the fields are updated
#     response = requests.get(BASE_URL + f"/booking/{booking_id}")
#     booking = response.json()
#     assert booking['firstname'] == 'Jane', "Name was not partially updated"
#
