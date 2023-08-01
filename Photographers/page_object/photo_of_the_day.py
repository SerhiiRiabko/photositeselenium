from selenium.webdriver.common.by import By

from Photographers.utilities.ui_utilities.base_page import BasePage


class PhotoOfTheDay(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __current_day_link = (By.XPATH, '//a[@href="/ratings/picturesday/1/"]')
    __page_title = (By.XPATH, '//h1')
    __dropdown_find = (By.XPATH, '//div/span/span[text()="Пошук"]')
    __find_photograph = (By.XPATH, '//li[1]/a[@href="https://photographers.ua/fotografy"]')
    __prof_photograph = (By.XPATH, '//li[@class="img-inline"]/a[@href="https://photographers.ua/professionalnye'
                                   '-fotografy"]/..')
    __model = (By.XPATH, '//li[@class="img-inline"]/a[@href="https://photographers.ua/modeli"]/..')
    __stylist = (By.XPATH, '//li[1]/a[@href="https://photographers.ua/vizazhisty-stilisty"]')
    __assistant_photographer = (By.XPATH, 'https://photographers.ua/assistenty-fotografa"]')
    __ard_director = (By.XPATH, '//li[1]/a[@href="https://photographers.ua/art-direktory"]')
    __studio_of_photo = (By.XPATH, '//li[1]/a[@href="https: // photographers.ua/fotostudii')

    def previous_day_photo_visible(self):
        self.find_element(self.__current_day_link)
        return self

    def page_title_visible(self):
        self.find_element(self.__page_title)
        return self

    def dropdown_is_visible(self):
        self.find_element(self.__dropdown_find)
        return self

    def dropdown_click(self):
        self.click(self.__dropdown_find)
        return self

    def find_photographs_link(self):
        self.find_element(self.__find_photograph)
        return self

    def find_prof_photographer(self):
        self.find_element(self.__prof_photograph)
        return self

    def find_model(self):
        self.find_element(self.__model)
        return self

    def find_stylist(self):
        self.find_element(self.__stylist)
        return self

    def find_assistant_photographer(self):
        self.find_element(self.__assistant_photographer)
        return self

    def find_art_director(self):
        self.find_element(self.__ard_director)
        return self

    def find_studio(self):
        self.find_element(self.__studio_of_photo)
        return self
