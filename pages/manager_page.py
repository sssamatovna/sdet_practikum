import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sdet_practikum.pages.base_page import BasePage
from sdet_practikum.pages.locators import ManagerLocators

class ManagerPage(BasePage):
    """Страница менеджера (общая навигация и Add Customer)."""

    def __init__(self, driver, base_url, path="/#/manager"):
        super().__init__(driver, base_url, path)

    @allure.step("Переход на вкладку 'Add Customer'")
    def go_to_add_customer(self):
        self.wait_visible(ManagerLocators.ADD_CUSTOMER_TAB).click()

    @allure.step("Переход на вкладку 'Customers'")
    def go_to_customers_list(self):
        self.wait_visible(ManagerLocators.CUSTOMERS_TAB).click()

    @allure.step("Добавление нового клиента: {fname} {lname} {postcode}")
    def add_customer(self, fname, lname, postcode):
        self.wait_visible(ManagerLocators.FIRST_NAME_INPUT).send_keys(fname)
        self.driver.find_element(*ManagerLocators.LAST_NAME_INPUT).send_keys(lname)
        self.driver.find_element(*ManagerLocators.POST_CODE_INPUT).send_keys(postcode)
        self.driver.find_element(*ManagerLocators.ADD_CUSTOMER_BTN).click()

        # Ждем и принимаем alert
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text