from selenium.webdriver.common.by import By
from Photographers.page_object.photo_of_the_day import PhotoOfTheDay
from Photographers.page_object.registration_page import RegisterPage
from Photographers.page_object.top_100_photo import Top100Photos
from Photographers.page_object.top_100_photographers import Top100Photographers
from Photographers.utilities.ui_utilities.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Elements at the page
    __site_logo = (By.XPATH, '//img[@alt="photographers.ua лого"]')
    __profile = (By.XPATH, '//a[@href="/SergeyRyabko/"]')
    __login = (By.XPATH, '//li/a[@id="btnShowLoginDialog"][@href="https://photographers.ua/user/login/"]')
    __registration = (By.XPATH, '//li/a[@class="register"]')
    __switch_to_english = (By.XPATH, '//a[@href="https://photographers.ua/stuff/lang/en/"]')
    __top_100_photographers = (By.XPATH, '//a[text()="ТОП 100 фотографів"]')
    __top_100_photos = (By.XPATH, '//a[text()="ТОП 100 фотографій"]')
    __photo_of_the_day = (By.XPATH, '//li/ul/li/a[@href="https://photographers.ua/ratings/picturesday/"]'
                                    '[text()="Картина дня"]')
    __email_input = (By.XPATH, '//input[@name="login"]')
    __password_input = (By.XPATH, '//input[@name="password"]')
    __login_in_form = (By.XPATH, '//button[@id="loginBtn"]')
    __profile_photo = (By.XPATH, '//li/a[@class="dropdown-toggle"]/img')
    __top_dropdown = (By.XPATH, '//a[@class="dropdown-toggle"][@href="https://photographers.ua/ratings/"]')

    def click_login_link(self):
        self.click(self.__login)
        return self

    def fill_email(self, email_value):
        self.send_keys(self.__email_input, email_value)
        return self

    def fill_pass(self, pass_value):
        self.send_keys(self.__password_input, pass_value)
        return self

    def click_login_bt(self):
        self.click(self.__login_in_form)
        return self

    def click_eng_switch(self):
        self.click(self.__switch_to_english)
        return self

    def check_logo_visible(self):
        self.find_element(self.__site_logo)
        return self

    def profile_visible(self):
        profile_data = self.find_element(self.__profile)
        actual_data_profile = profile_data.get_attribute("href")
        return actual_data_profile

    def click_registration_link(self):
        self.click(self.__registration)
        return RegisterPage(self._driver)

    def click_profile_photo(self):
        self.click(self.__profile_photo)
        return self

    def move_top_dropdown(self):
        self.move_on_element(self.__top_dropdown)
        return self

    def click_top_100_photos(self):
        self.click(self.__top_100_photos)
        return Top100Photos(self._driver)

    def click_top_100_photographers(self):
        self.click(self.__top_100_photographers)
        return Top100Photographers(self._driver)

    def click_photo_of_the_day(self):
        self.click(self.__photo_of_the_day)
        return PhotoOfTheDay(self._driver)
