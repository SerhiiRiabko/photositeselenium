from selenium.webdriver.common.by import By
from Photographers.utilities.ui_utilities.base_page import BasePage


class PhotoOfTheDay(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __current_day_link = (By.XPATH, '//a[@href="/ratings/picturesday/1/"]')

    def previous_day_photo_visible(self):
        previous_day_button = self.find_element(self.__current_day_link)
        return previous_day_button
