from selenium.webdriver.support.wait import WebDriverWait
from Photographers.page_object.main_page import MainPage
from Photographers.utilities.config_reader import ReadConfig


def test_page_email_wait(create_driver):
    driver = create_driver
    WebDriverWait(driver, 10)
    actual_page = driver.title  # main page
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
    assert photo_of_the_day_page.previous_day_photo_visible(), "This is not page today photo of the day"


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


def test_check_open_page_photo_of_the_day(create_driver):
    driver = create_driver
    photo_of_the_day_page = MainPage(driver).click_about_project_link().click_photo_day_link()
    assert photo_of_the_day_page.page_title_visible(), "Page is not opened"


def test_check_news_link(create_driver):
    driver = create_driver
    about_the_project_page = MainPage(driver).click_about_project_link()
    assert about_the_project_page.check_news_link_visible(), "The link as at the page"


def test_email_link_visible(create_driver):
    driver = create_driver
    about_project_page = MainPage(driver).click_about_project_link()
    assert about_project_page.check_email_visible(), "Email is not at the page"


def test_site_link_visible(create_driver):
    driver = create_driver
    about_project_page = MainPage(driver).click_about_project_link()
    assert about_project_page.check_link_site_visible()


def test_main_page_from_about(create_driver):
    driver = create_driver
    main_page = MainPage(driver).click_about_project_link().click_site_link()
    assert main_page.check_24_hours_title_visible(), "No title at the page. Incorrect page"


def test_registration_link_in_text(create_driver):
    driver = create_driver
    about_project_page = MainPage(driver).click_about_project_link()
    assert about_project_page.check_register_link_visible(), "Link is not shown at the page"


def test_about_page_title_visible(create_driver):
    driver = create_driver
    about_project_page = MainPage(driver).click_about_project_link()
    assert about_project_page.title_page_visible()


def test_photograph_link_is_visible(create_driver):
    driver = create_driver
    photo_of_the_day = MainPage(driver).click_photo_of_the_day().dropdown_click()
    assert photo_of_the_day.find_photographs_link(), "Link photographer is not presented"


def test_model_link_is_visible(create_driver):
    driver = create_driver
    photo_of_the_day = MainPage(driver).click_photo_of_the_day().dropdown_click()
    assert photo_of_the_day.find_model(), "Link model is not presented"


def test_find_pro_photographer_link_is_visible(create_driver):
    driver = create_driver
    photo_of_the_day = MainPage(driver).click_photo_of_the_day().dropdown_click()
    assert photo_of_the_day.find_prof_photographer(), "Link PRO photographer is not presented"


def test_login_by_google(create_driver):
    driver = create_driver
    registration_page = MainPage(driver).click_registration_link()
    assert registration_page.login_by_google_visible(), "Link fo registration by Google is not presented"


def test_login_by_facebook(create_driver):
    driver = create_driver
    registration_page = MainPage(driver).click_registration_link()
    assert registration_page.login_by_facebook_visible(), "Link fo registration by FaceBook is not presented"


def test_ingo_block_at_the_page(create_driver):
    driver = create_driver
    registration_page = MainPage(driver).click_registration_link()
    assert registration_page.why_register_block_visible(), "Information block is not presented"


def test_check_next_month_link(create_driver):
    driver = create_driver
    top_100_photographers_page = MainPage(driver).move_top_dropdown().click_top_100_photographers()
    assert top_100_photographers_page.check_link_is_not_at_the_page() is True, "The link is  at the page for" \
                                                                               " future month"


def test_check_first_month_results(create_driver):
    driver = create_driver
    top_100_photographers_page = MainPage(driver).move_top_dropdown().click_top_100_photographers()
    assert top_100_photographers_page.check_search_by_months(), "January is in the list"


def test_switch_to_eng_link(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    assert main_page.find_eng_switch(), "Link for switch language is at the page"


def test_switch_to_eng(create_driver):
    driver = create_driver
    main_page = MainPage(driver).click_eng_switch()
    assert main_page.check_gallery_element_visible_text() == "Gallery", "Not English text at the site"
