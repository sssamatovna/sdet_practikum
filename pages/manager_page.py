import allure
from typing import List, Dict
from sdet_practikum.pages.base_page import BasePage
from sdet_practikum.pages.locators import ManagerPageLocators, CustomersLocators

class ManagerPage(BasePage):
    path = "/angularJs-protractor/BankingProject/#/manager"

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url, self.path)

    # ---- Manager tab ----
    @allure.step("Нажать на кнопку 'Add Customer'")
    def click_add_customer_button(self) -> None:
        self.click_element(ManagerPageLocators.ADD_CUSTOMER_BUTTON)

    @allure.step("Заполнить форму клиента: {first_name} {last_name}, {post_code}")
    def fill_customer_form(self, first_name: str, last_name: str, post_code: str) -> None:
        self.fill_field(ManagerPageLocators.FIRST_NAME, first_name)
        self.fill_field(ManagerPageLocators.LAST_NAME, last_name)
        self.fill_field(ManagerPageLocators.POST_CODE, post_code)

    @allure.step("Отправить форму 'Add Customer'")
    def submit_customer_form(self) -> None:
        self.click_element(ManagerPageLocators.SUBMIT_BUTTON)

    # ---- Customers tab ----
    @allure.step("Перейти на вкладку 'Customers'")
    def go_to_customers_tab(self) -> None:
        self.click_element(ManagerPageLocators.CUSTOMERS_BUTTON)
        self.find_element(CustomersLocators.CUSTOMERS_TABLE)

    @allure.step("Клик по заголовку First Name для сортировки")
    def sort_by_first_name(self) -> None:
        self.click_element(CustomersLocators.HEADER_FIRST_NAME)

    @allure.step("Применить фильтр поиска по имени: {query}")
    def search_customer(self, query: str) -> None:
        self.fill_field(CustomersLocators.SEARCH_INPUT, query)

    @allure.step("Получить список имён из таблицы")
    def get_all_first_names(self) -> List[str]:
        rows = self.find_elements(CustomersLocators.TABLE_ROWS)
        names: List[str] = []
        for r in rows:
            names.append(r.find_element(*CustomersLocators.CELL_FIRST_NAME).text)
        return names

    @allure.step("Получить данные из последней строки таблицы")
    def get_last_row_data(self) -> Dict[str, str]:
        rows = self.find_elements(CustomersLocators.TABLE_ROWS)
        last = rows[-1]
        return {
            "first_name": last.find_element(*CustomersLocators.CELL_FIRST_NAME).text,
            "last_name":  last.find_element(*CustomersLocators.CELL_LAST_NAME).text,
            "post_code":  last.find_element(*CustomersLocators.CELL_POST_CODE).text,
        }

    @allure.step("Удалить строку, где имя = {first_name}")
    def delete_by_first_name(self, first_name: str) -> None:
        rows = self.find_elements(CustomersLocators.TABLE_ROWS)
        for row in rows:
            if row.find_element(*CustomersLocators.CELL_FIRST_NAME).text == first_name:
                row.find_element(*CustomersLocators.CELL_DELETE_BTN).click()
                return