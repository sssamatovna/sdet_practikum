import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import ManagerLocators

class ManagerPage(BasePage):
    """Страница менеджера (общая навигация и Add Customer)."""

    def __init__(self, driver, base_url, path="/#/manager"):
        super().__init__(driver, base_url, path)

    @allure.step("Переход на вкладку 'Add Customer'")
    def go_to_add_customer(self):
        self.click_element(ManagerLocators.ADD_CUSTOMER_TAB)

    @allure.step("Переход на вкладку 'Customers'")
    def go_to_customers_list(self):
        self.click_element(ManagerLocators.CUSTOMERS_TAB)

    @allure.step("Добавление нового клиента: {fname} {lname} {postcode}")
    def add_customer(self, fname, lname, postcode):
        self.fill_field(ManagerLocators.FIRST_NAME_INPUT, fname)
        self.fill_field(ManagerLocators.LAST_NAME_INPUT, lname)
        self.fill_field(ManagerLocators.POST_CODE_INPUT, postcode)
        self.click_element(ManagerLocators.ADD_CUSTOMER_BTN)

        # Ждем и принимаем alert
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text
