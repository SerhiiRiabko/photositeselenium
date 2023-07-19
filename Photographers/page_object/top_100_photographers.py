from selenium.webdriver.common.by import By

from Photographers.utilities.ui_utilities.base_page import BasePage


class Top100Photographers(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __page_text_title = (By.XPATH, '//h1')
    __users_in_list = (By.XPATH, '//tbody/tr/td[@class="text avatar"]')

    def page_text_title(self):
        text_title = self.find_element(self.__page_text_title)
        text = text_title.text
        return text

    def quantity_of_elements(self):
        elements_at_page = self.find_elements(self.__users_in_list)
        quantity = len(elements_at_page)
        return quantity
