import allure
from selenium.webdriver.common.by import By
from sdet_practikum.pages.base_page import BasePage
# Используем импортированный класс локаторов
from sdet_practikum.pages.locators import CustomersLocators


class CustomersPage(BasePage):

    def __init__(self, driver, base_url, path="/#/manager/list"):
        super().__init__(driver, base_url, path)

    @allure.step("Получение списка имен клиентов из таблицы")
    def get_all_first_names(self) -> list:
        self._wait_visible(CustomersLocators.CUSTOMER_TABLE_ROWS)

        elements = self.driver.find_elements(*CustomersLocators.FNAME_CELLS)

        names = [elem.text for elem in elements if elem.text]
        return names

    @allure.step("Сортировка списка по 'First Name'")
    def sort_by_first_name(self):
        self.click_element(CustomersLocators.SORT_BY_FNAME_LINK)

    @allure.step("Удаление клиента по имени: {name}")
    def delete_by_first_name(self, name):
        delete_button_xpath = (By.XPATH, f"//table/tbody/tr[td[1]='{name}']/td[5]/button")


        self.click_element(delete_button_xpath)