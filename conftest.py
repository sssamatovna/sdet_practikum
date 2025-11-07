import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from sdet_practikum.pages.base_page import BasePage
from sdet_practikum.pages.manager_page import ManagerPage
from sdet_practikum.utils import random_data
import random
import allure


@pytest.fixture(scope="session")
def base_url():
    return "https://www.globalsqa.com/angularJs-protractor/BankingProject"


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_test_customers(driver, base_url):
    manager_page = ManagerPage(driver, base_url, path="/#/manager")
    manager_page.open()

    required_lengths = [5, 7, 9]
    names_to_add = []

    with allure.step(f"Создание клиентов с длинами имен {required_lengths}"):
        for length in required_lengths:
            # Используем новую функцию для генерации имени нужной длины
            name = random_data.generate_name_by_length(length)

            # Добавляем клиента
            manager_page.go_to_add_customer()
            # Используем случайный, но уникальный Post Code
            post_code = str(random.randint(1000000000, 9999999999))
            manager_page.add_customer(name, "Sdet", post_code)

            names_to_add.append(name)

    return names_to_add