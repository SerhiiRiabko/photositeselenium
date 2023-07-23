from Photographers.utilities.api_utilities.base_api import BaseAPI


class BookingAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.__booking_url = '/booking'

    def get_booking_by_id(self, booking_id, headers=None):
        response = self.get(f'{self.__booking_url}/{booking_id}', headers = headers)
        return response

    def create_booking(self, booking, headers=None):
        response = self.post(self.__booking_url, booking.get_dict(), headers=headers)
        return response
