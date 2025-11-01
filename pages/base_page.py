import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, driver, base_url, path=""):
        self.driver = driver
        self.base_url = base_url
        self.path = path
        self.url = f"{base_url}{path}"

    @allure.step("Открыть страницу")
    def open(self):
        """Открывает страницу и ждет ее базовой загрузки."""
        self.driver.get(self.url)
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button[ng-click='addCust()']")
            )
        )

    def find_element(self, locator, time=DEFAULT_TIMEOUT):
        """Находит один элемент, ожидая его видимости."""
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}",
        )

    def find_elements(self, locator, time=DEFAULT_TIMEOUT):
        """Находит все элементы, ожидая их видимости."""
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Не удалось найти элементы по локатору {locator}",
        )