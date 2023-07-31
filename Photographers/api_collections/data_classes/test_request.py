import requests
from Photographers.api_collections.data_classes.change_data import ChangeData

url = 'https://restful-booker.herokuapp.com/booking/1'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'token abc123'
}

booking_data = ChangeData(firstname="James", lastname="Brown", totalprice=111, depositpaid=True,
                          bookingdates={"checkin": "2018-01-01", "checkout": "2019-01-01"},
                          additionalneeds="Breakfast")

response = requests.put(url, headers=headers, json=booking_data.get_dict())
