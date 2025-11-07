import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from sdet_practikum.pages.manager_page import ManagerPage
from sdet_practikum.pages.customers_page import CustomersPage
from sdet_practikum.utils import random_data


@pytest.fixture(scope="session")
def base_url():
    return "https://www.globalsqa.com/angularJs-protractor/BankingProject"


@pytest.fixture(scope="function")
def driver():
    options = Options()
  
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options 
    )
    
    driver.implicitly_wait(10) 
  
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_test_customers(driver, base_url):
    """
    Фикстура для создания трех клиентов с именами, имеющими длины 5, 7 и 9.
    Возвращает список этих сгенерированных имен.
    """
    manager_page = ManagerPage(driver, base_url, path="/#/manager")
    manager_page.open()
    

    required_lengths = [5, 7, 9]
    names_to_add = []
    
    with allure.step(f"Создание клиентов с длинами имен {required_lengths}"):
        for length in required_lengths:

            name = data_generator.generate_name_by_length(length)
            

            manager_page.go_to_add_customer()

            post_code = str(random.randint(1000000000, 9999999999))
            manager_page.add_customer(name, "GenTest", post_code)
            
            names_to_add.append(name)

    return names_to_add
