from typing import Tuple
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from settings import DEFAULT_TIMEOUT


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

    @allure.step("Открыть страницу")
    def open(self) -> None:
        with allure.step(f"GET {self.url}"):
            self.driver.get(self.url)
            # Ожидание загрузки тела страницы (можно заменить на более специфичный локатор)
            WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

    def _wait_visible(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        """Ждет, пока элемент станет видимым, и возвращает его."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"Ошибка ожидания {locator}",
                          attachment_type=allure.attachment_type.PNG)
            raise TimeoutException(f"Элемент с локатором {locator} не стал видимым за {timeout} секунд.") from e

    def _wait_clickable(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        """Ждет, пока элемент станет кликабельным, и возвращает его."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"Ошибка ожидания клика {locator}",
                          attachment_type=allure.attachment_type.PNG)
            raise TimeoutException(f"Элемент с локатором {locator} не стал кликабельным за {timeout} секунд.") from e


    @allure.step("Клик по элементу с локатором {locator}")
    def click_element(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT) -> None:
        """Ждет, пока элемент станет кликабельным, и кликает по нему."""
        element = self._wait_clickable(locator, timeout)
        element.click()

    @allure.step("Заполнение поля {locator} текстом: '{text}'")
    def fill_field(self, locator: Tuple[str, str], text: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Ждет, пока поле станет видимым, очищает его и заполняет текстом."""
        element = self._wait_visible(locator, timeout)

        element.clear()

        element.send_keys(text)
