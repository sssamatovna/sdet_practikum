import allure
from selenium.webdriver.common.by import By
from sdet_practikum.pages.base_page import BasePage
from sdet_practikum.pages.locators import CustomersLocators


class CustomersPage(BasePage):

    def __init__(self, driver, base_url, path="/#/manager/list"):
        super().__init__(driver, base_url, path)

    @allure.step("Получение списка имен клиентов из таблицы")
    def get_all_first_names(self) -> list:
        try:
            self.wait_visible(CustomersLocators.CUSTOMER_TABLE_ROWS)

            elements = self.driver.find_elements(*CustomersLocators.FNAME_CELLS)
            names = [elem.text for elem in elements]
            return names
        except Exception:
            return []

    @allure.step("Сортировка списка по 'First Name'")
    def sort_by_first_name(self):
        self.driver.find_element(*CustomersLocators.SORT_BY_FNAME_LINK).click()

    @allure.step("Удаление клиента по имени: {name}")
    def delete_by_first_name(self, name):
        delete_button_xpath = f"//table/tbody/tr[td[1]='{name}']/td[5]/button"

        try:
            delete_button = self.wait_visible((By.XPATH, delete_button_xpath))
            delete_button.click()
        except Exception as e:
            raise AssertionError(f"Не удалось найти или нажать кнопку 'Delete' для клиента {name}: {e}")