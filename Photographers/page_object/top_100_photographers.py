from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from Photographers.utilities.ui_utilities.base_page import BasePage


class Top100Photographers(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    current_month = datetime.today().month
    next_month_date = datetime.today() + timedelta(days=30)
    next_month = next_month_date.month

    if next_month == 1:
        next_month_ukr = "січень"
    elif  next_month == 2:
        next_month_ukr = "лютий"
    elif next_month == 3:
        next_month_ukr = "березень"
    elif next_month == 4:
        next_month_ukr = "квітень"
    elif next_month == 5:
        next_month_ukr = "травень"
    elif next_month == 6:
        next_month_ukr = "червень"
    elif next_month == 7:
        next_month_ukr = "липень"
    elif next_month == 8:
        next_month_ukr = "серпень"
    elif next_month == 9:
        next_month_ukr = "вересень"
    elif next_month == 10:
        next_month_ukr = "жовтень"
    elif next_month == 11:
        next_month_ukr = "листопад"
    elif next_month == 12:
        next_month_ukr = "грудень"
    else:
        print('Incorrect value')


    __page_text_title = (By.XPATH, '//h1')
    __users_in_list = (By.XPATH, '//tbody/tr/td[@class="text avatar"]')
    __random_photo_link = (By.XPATH, '//div[@class="b-random-photo b-random-photo-right-col"]/a')
    __download_top_100_photographers = (By.XPATH, '//div[@class="pdf"]/a')
    __january_results_link = (By.XPATH, '//tr[@class="top100users "]/td/a[text()="січень"]')
    __next_month_link = (By.XPATH, f'//tr[@class="top100users "]/td/a[text()="{next_month}"]')
    __ukraine_raiting_link = (By.XPATH, '//span[@class="nobr"]/a[text()="Україна"]')
    __usa_rating_link = (By.XPATH, '//span[@class="nobr"]/a[text()="США"]')
    __new_photos = (By.XPATH, '//div[@class="b-new-photos"]')

    def page_text_title(self):
        text_title = self.find_element(self.__page_text_title)
        text = text_title.text
        return text

    def quantity_of_elements(self):
        elements_at_page = self.find_element(self.__users_in_list)
        quantity = len(elements_at_page)
        return quantity

    def random_photo_link_visible(self):
        self.find_element(self.__random_photo_link)
        return self

    def link_for_download_results(self):
        self.find_element(self.__download_top_100_photographers)
        return self

    def check_search_by_months(self):
        self.click(self.__january_results_link)
        return self

    def check_link_is_not_at_the_page(self):
        return self.no_element(self.__next_month_link)  # return False

    def check_link_ukr_photographer_visible(self):
        self.find_element(self.__ukraine_raiting_link)
        return self

    def check_link_usa_photographer_visible(self):
        self.find_element(self.__usa_rating_link)
        return self

    def area_is_visible(self):
        self.find_element(self.__new_photos)
        return self
