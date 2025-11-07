# conftest.py

import pytest
import random
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from sdet_practikum.pages.base_page import BasePage
from sdet_practikum.pages.manager_page import ManagerPage
from sdet_practikum.utils import random_data
from sdet_practikum.base_data import BASE_URL 


@pytest.fixture(scope="session")
def base_url():
    """Возвращает базовый URL приложения."""
    return BASE_URL

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox") # Важно для CI
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080") # Задаем размер окна для headless-режима
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options 
    )
    
    driver.maximize_window() 
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="function")
def create_test_customers(driver, base_url):
    """Создает трех клиентов с разными длинами имен и возвращает список их имен."""
    manager_page = ManagerPage(driver, base_url, path="/#/manager")
    manager_page.open()

    required_lengths = [5, 7, 9]
    names_to_add = []

    with allure.step(f"Создание клиентов с длинами имен {required_lengths}"):
        for length in required_lengths:
            name = random_data.generate_name_by_length(length)

            manager_page.go_to_add_customer()
            post_code = str(random.randint(1000000000, 9999999999))
            manager_page.add_customer(name, "Sdet", post_code)

            names_to_add.append(name)

    return names_to_add
