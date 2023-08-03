from selenium.webdriver.common.by import By

from Photographers.utilities.ui_utilities.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __register_email_field = (By.XPATH, '//input[@name="user[strEmail]"]')
    __register_password_field = (By.XPATH, '//input[@name="user[strPassword]"]')
    __full_name_field = (By.XPATH, '//input[@name="user[strUserName]"]')
    __register_bt = (By.XPATH, '//input[@name="submit"]')
    __register_approve_msg = (By.XPATH, '//td/p[1]')  # No ability without index
    __error_message = (By.XPATH, '//div[@role="alert"]')

    def fill_email(self, email_value):
        self.send_keys(self.__register_email_field, email_value)
        return self

    def fill_pass(self, pass_value):
        self.send_keys(self.__register_password_field, pass_value)
        return self

    def fill_name(self, name_value):
        self.send_keys(self.__full_name_field, name_value)
        return self

    def click_register_bt(self):
        self.click(self.__register_bt)
        return self

    def success_register_message(self):
        register_message = self.find_element(self.__register_approve_msg)
        text_message = register_message.text
        return text_message

    def inform_error_message(self):
        msg_element = self.find_element(self.__error_message)
        return msg_element
