from selenium.webdriver.support.wait import WebDriverWait

from Selenium_for_site.page_objects.main_page import MainPage
from Selenium_for_site.utilities.config_reader import ReadConfig


def test_page_email_wait(create_driver):
    driver = create_driver
    WebDriverWait(driver, 10)

    actual_page = driver.title
    assert actual_page == "Інтернет-магазин ROZETKA™: офіційний сайт найпопулярнішого онлайн-гіпермаркету в Україні", \
        'Text of title is not as in requirements'


def test_login(create_driver):
    email, password = ReadConfig.get_user_creds()
    driver = create_driver
    main_page = MainPage(driver).click_user_icon().fill_email(email).fill_pass.click_login().click_burger_menu()
