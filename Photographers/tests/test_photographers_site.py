from selenium.webdriver.support.wait import WebDriverWait

from Photographers.page_object.main_page import MainPage
from Photographers.utilities.config_reader import ReadConfig


def test_page_email_wait(create_driver):
    driver = create_driver
    WebDriverWait(driver, 10)

    actual_page = driver.title
    assert actual_page == "Фотографи, моделі, візажисти, стилісти, фотостудії та їх фото / photographers.ua", \
        "Text is not correspond requirements"


def test_login(create_driver):
    email, password = ReadConfig.get_user_creds()
    driver = create_driver
    main_page = MainPage(driver).click_user_icon().fill_email(email).fill_pass.click_login().click_burger_menu()
