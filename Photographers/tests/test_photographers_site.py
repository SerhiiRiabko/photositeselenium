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
    main_page = MainPage(driver).click_login_link().fill_email(email).fill_pass(password).click_login_bt() \
        .click_profile_photo()
    assert main_page.profile_visible() == user_icon_link, "No profile"


def test_registration_ok(create_driver):
    email, password, full_name = ReadConfig.get_user_register_data()
    driver = create_driver
    registration_page = MainPage(driver).click_registration_link().fill_email(email).fill_pass(password). \
        fill_name(full_name).click_register_bt()
    assert registration_page.success_register_message() == "Реєстрація пройшла успішно! Вам було надіслано листа із " \
                                                           "посиланням активації для підтвердження існування введеної" \
                                                           " Вами адреси.", "Registration failed"


def test_registration_fail_user_is_in_base(create_driver):
    email, password, full_name = ReadConfig.get_user_register_data()
    driver = create_driver
    registration_page = MainPage(driver).click_registration_link().fill_email(email).fill_pass(password). \
        fill_name(full_name).click_register_bt()
    assert registration_page.inform_error_message().is_displayed(), "User registered"
