import requests

url = 'https://restful-booker.herokuapp.com/booking/1'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'token abc123'
}

response = requests.put(url, headers=headers, json={
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
})

print(response.status_code)
print(response.text)