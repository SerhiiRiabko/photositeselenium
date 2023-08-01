from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._actions = ActionChains(driver)
        #self._find = webdriver.Chrome().find_elements(self, driver)

   # def find_elements(self, locator: tuple):
   #     return self._find(EC.visibility_of_element_located(locator))

    def __wait_until_element_visible(self, locator: tuple):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_clickable(self, locator: tuple):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator, value, is_clear=True):
        element = self.__wait_until_element_visible(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def click(self, locator):
        self.__wait_until_element_clickable(locator).click()

    def find_element(self, locator: tuple):
        return self.__wait_until_element_visible(locator)

    def no_element(self, locator: tuple):
        return self._wait.until(EC.invisibility_of_element_located(locator))

    def move_on_element(self, locator: tuple):
        element = self.__wait_until_element_visible(locator)
        return self._actions.move_to_element(element).perform()
