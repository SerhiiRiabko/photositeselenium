import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Photographers.utilities.config_reader import ReadConfig
from Photographers.utilities.ui_utilities.base_page import BasePage

@pytest.fixture
def create_driver(request):
    # Add your code to create a WebDriver instance here
    # You can use a fixture to create the driver and ensure it's closed after the test
    # For example, if you're using Chrome WebDriver:

    driver = create_chrome_driver()  # Replace this with your WebDriver creation logic

    def close_driver():
        driver.quit()

    request.addfinalizer(close_driver)
    return driver

def test_page_email_wait(create_driver):
    driver = create_driver
    actual_page = driver.title
    assert actual_page == "Інтернет-магазин ROZETKA™: офіційний сайт найпопулярнішого онлайн-гіпермаркету в Україні"

def test_human_conversion_to_json_and_xml():
    # Load configuration from config.json
    config = ConfigReader.get_config()

    human = Human(config["name"], config["age"], config["gender"], config["birth_year"])

    # Convert to JSON
    json_data = human.convert_to_json()
    print("JSON representation:")
    print(json_data)

    # Convert to XML
    xml_data = human.convert_to_xml()
    print("XML representation:")
    print(xml_data)

    # Optionally, write to files
    with open('human.json', 'w') as json_file:
        json_file.write(json_data)

    with open('human.xml', 'w') as xml_file:
        xml_file.write(xml_data)