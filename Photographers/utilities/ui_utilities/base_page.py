from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

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


