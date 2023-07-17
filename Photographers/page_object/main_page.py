from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Photographers.utilities.ui_utilities.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Elements at the page
    __site_logo = (By.XPATH, '//img[@alt="photographers.ua лого"]')
    __profile = (By.XPATH, '//a[@href="/SergeyRyabko/"]')
    __login = (By.XPATH, '//a[@id="btnShowLoginDialog"]')
    __registration = (By.XPATH, '//li/a[@class="register"]')
    __switch_to_english = (By.XPATH, '//a[@href="https://photographers.ua/stuff/lang/en/"]')
    __top_100 = (By.XPATH, '//a[text()="ТОП 100 фотографів"]')

    def click_login_bt(self):
        login_bt = self._wait.until(EC.visibility_of_element_located(self.__login))
        login_bt.click(self)

