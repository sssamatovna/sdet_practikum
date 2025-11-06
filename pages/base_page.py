# sdet_practikum/pages/base_page.py
from typing import List, Tuple
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from sdet_practikum.settings import DEFAULT_TIMEOUT

class BasePage:
    driver: WebDriver
    base_url: str
    path: str
    url: str

    def __init__(self, driver: WebDriver, base_url: str, path: str = "") -> None:
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.path = path
        self.url = f"{self.base_url}{self.path}"

    # ВАЖНО: без плейсхолдеров {self.*} в декораторе!
    @allure.step("Открыть страницу менеджера")
    def open(self) -> None:
        with allure.step(f"GET {self.url}"):
            self.driver.get(self.url)
            WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[ng-click='addCust()']"))
            )

    # ---- helpers ----
    def wait_visible(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_all_visible(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def find_element(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        return self.wait_visible(locator, timeout)

    def find_elements(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        return self.wait_all_visible(locator, timeout)

    def click_element(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT) -> None:
        self.wait_visible(locator, timeout).click()

    def fill_field(self, locator: Tuple[str, str], text: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        el = self.wait_visible(locator, timeout)
        el.clear()
        el.send_keys(text)

    def get_texts(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT) -> List[str]:
        return [e.text for e in self.find_elements(locator, timeout)]

    def is_present(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT) -> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Подтвердить браузерный alert")
    def accept_alert(self) -> str:
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text