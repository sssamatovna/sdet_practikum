import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from settings import DEFAULT_LAST_NAME
from pages.manager_page import ManagerPage
from tests.utils import generate_customer_data

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("BASE_URL")
    if not url:
        pytest.fail("Переменная окружения BASE_URL не задана в .env файле")
    return url


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()

    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-proxy-server")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()


@pytest.fixture(scope="function")
def create_three_customers(driver, base_url):

    name_lengths = [3, 5, 7]

    for length in name_lengths:
        manager_page = ManagerPage(driver, base_url)
        if driver.current_url != manager_page.url:
            manager_page.open()

        manager_page.click_add_customer_button()
        first_name, post_code = generate_customer_data(name_length=length)
        manager_page.fill_customer_form(
            first_name, DEFAULT_LAST_NAME, post_code
        )  # noqa: E501
        manager_page.submit_customer_form()
        manager_page.accept_alert()