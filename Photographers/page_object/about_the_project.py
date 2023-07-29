from selenium.webdriver.common.by import By

#from Photographers.page_object.main_page import MainPage
from Photographers.page_object.photo_of_the_day import PhotoOfTheDay
from Photographers.page_object.registration_page import RegisterPage
from Photographers.page_object.top_100_photo import Top100Photos
from Photographers.page_object.top_100_photographers import Top100Photographers
from Photographers.utilities.ui_utilities.base_page import BasePage


class AboutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __title_page = (By.XPATH, '//div[@class="b-post"]/h1')
    __link_for_register = (By.XPATH, '//div[@class="typo"]/p/a[text()="створити свій профайл"]')
    __main_page = (By.XPATH, '//div[@class="typo"]/p/a[text()="photographers.ua"]')
    __site_news = (By.XPATH, '//a/strong[text()="«Новини сайту»"]')
    __address_email = (By.XPATH, '//td/a[@class="email"]')
    __photo_of_the_day = (By.XPATH, '//ul[@class="b-navigation"]/li/a[text()="Картина дня"]')
    __top_photo = (By.XPATH, '//ul[@class="b-navigation"]/li/a[text()="Топ фотографій"]')
    __top_photographers = (By.XPATH, '//ul[@class="b-navigation"]/li/a[text()="Топ користувачів"]')
    __switch_to_english = (By.XPATH, '//a[@href="https://photographers.ua/stuff/lang/en/"]')
    __site_logo = (By.XPATH, '//img[@alt="photographers.ua лого"]')

    def check_logo_visible(self):
        self.find_element(self.__site_logo)
        return self

    def click_logo(self):
        self.click(self.__site_logo)
        from Photographers.page_object.main_page import MainPage
        return MainPage(self._driver)

    def click_switch_language(self):
        self.click(self.__switch_to_english)
        return self

    def click_top_users_link(self):
        self.click(self.__top_photographers)
        return Top100Photographers(self._driver)

    def click_top_photo_link(self):
        self.click(self.__top_photo)
        return Top100Photos(self._driver)

    def click_photo_day_link(self):
        self.click(self.__photo_of_the_day)
        return PhotoOfTheDay(self._driver)

    def check_email_visible(self):
        self.find_element(self.__address_email)
        return self

    def check_link_site_visible(self):
        self.find_element(self.__main_page)
        return self

    def click_site_link(self):
        self.click(self.__main_page)
        from Photographers.page_object.main_page import MainPage
        return MainPage(self._driver)

    def check_news_link_visible(self):
        self.find_element(self.__site_news)
        return self

    def check_register_link_visible(self):
        self.find_element(self.__link_for_register)
        return self

    def register_link_click(self):
        self.click(self.__link_for_register)
        return RegisterPage(self._driver)

    def title_page_visible(self):
        self.find_element(self.__title_page)
        return self
