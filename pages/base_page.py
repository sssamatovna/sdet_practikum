from typing import Tuple
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sdet_practikum.settings import DEFAULT_TIMEOUT


class BasePage:

    def __init__(self, driver: WebDriver, base_url: str, path: str = "") -> None:
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.path = path
        self.url = f"{self.base_url}{self.path}"

    @allure.step("Открыть страницу")
    def open(self) -> None:
        with allure.step(f"GET {self.url}"):
            self.driver.get(self.url)
            WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[ng-click='addCust()']"))
            )

    # ---- helpers ----
    def wait_visible(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        """Ожидает видимости элемента по локатору."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )