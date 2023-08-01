from Photographers.utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class Top100Photos(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __page_text_title = (By.XPATH, '//h1')

    def page_text_title(self):
        text_title = self.find_element(self.__page_text_title)
        text = text_title.text
        return text
