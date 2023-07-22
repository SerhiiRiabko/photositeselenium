from selenium.webdriver.support.wait import WebDriverWait
from Photographers.page_object.main_page import MainPage
from Photographers.utilities.config_reader import ReadConfig


def test_page_email_wait(create_driver):
    driver = create_driver
    WebDriverWait(driver, 10)
    actual_page = driver.title
    assert actual_page == 'Фотографи, моделі, візажисти, стилісти, фотостудії та їх фото / photographers.ua'


def test_login(create_driver, env):
    email, password = env.email, env.password
    user_icon_link = env.link_photo
    driver = create_driver
    main_page = MainPage(driver).click_login_link().fill_email(email).fill_pass(password).click_login_bt() \
        .click_profile_photo()
    assert main_page.profile_visible() == user_icon_link, "No profile"


def test_registration_ok(create_driver, env):
    email, password, full_name = env.email, env.password, env.full_name
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


def test_no_button_next_day(create_driver):
    driver = create_driver
    photo_of_the_day_page = MainPage(driver).move_top_dropdown().click_photo_of_the_day()
    assert photo_of_the_day_page.previous_day_photo_visible().is_displayed(), "This is not page today photo of the day"


def test_text_title_of_page_100_photographers(create_driver):
    driver = create_driver
    top_100_photographers_page = MainPage(driver).move_top_dropdown().click_top_100_photographers()
    expected_text = "ТОП 100 фотографів"
    assert expected_text in top_100_photographers_page.page_text_title(), "Part of text is not presented at the title"


def test_text_title_of_page_100_photos(create_driver):
    driver = create_driver
    top_100_photos_page = MainPage(driver).move_top_dropdown().click_top_100_photos()
    expected_text = "ТОП 100 Фотографій"
    assert expected_text in top_100_photos_page.page_text_title(), "Part of text is not presented at the title"


def test_check_quantity_in_list_of_photographers(create_driver):
    driver = create_driver
    top_100_photographers_page = MainPage(driver).move_top_dropdown().click_top_100_photographers()
    expected_quantity = 100
    assert expected_quantity == top_100_photographers_page.quantity_of_elements(), "There are no 100 Photographers"
