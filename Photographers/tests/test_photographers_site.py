from selenium.webdriver.support.wait import WebDriverWait

from Photographers.page_object.main_page import MainPage
from Photographers.utilities.config_reader import ReadConfig


def test_page_email_wait(create_driver):
    driver = create_driver
    WebDriverWait(driver, 10)
    actual_page = driver.title
    assert actual_page == 'Фотографи, моделі, візажисти, стилісти, фотостудії та їх фото / photographers.ua'


def test_login(create_driver):
    email, password = ReadConfig.get_user_creds()
    user_icon_link = ReadConfig.get_photo_link()
    driver = create_driver
    main_page = MainPage(driver).click_login_link().fill_email(email).fill_pass(password).click_login_bt()\
        .click_profile_photo()
    assert main_page.profile_visible() == user_icon_link, "No profile"
