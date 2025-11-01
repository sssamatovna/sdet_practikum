import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ManagerPageLocators


class ManagerPage(BasePage):
    path = "/angularJs-protractor/BankingProject/#/manager"

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url, self.path)

    @allure.step("Нажать на кнопку 'Add Customer'")
    def click_add_customer_button(self):
        self.find_element(ManagerPageLocators.ADD_CUSTOMER_BUTTON).click()

    @allure.step(
        "Заполнить форму клиента: "
        "Имя={first_name},"
        "Фамилия={last_name},"
        "Индекс={post_code}"
    )
    def fill_customer_form(self, first_name, last_name, post_code):
        self.find_element(ManagerPageLocators.FIRST_NAME).send_keys(first_name)
        self.find_element(ManagerPageLocators.LAST_NAME).send_keys(last_name)
        self.find_element(ManagerPageLocators.POST_CODE).send_keys(post_code)

    @allure.step("Нажать 'Add Customer' для отправки формы")
    def submit_customer_form(self):
        self.find_element(ManagerPageLocators.SUBMIT_BUTTON).click()

    @allure.step("Принять alert после добавления клиента")
    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    @allure.step("Перейти на вкладку 'Customers'")
    def go_to_customers_tab(self):
        self.find_element(ManagerPageLocators.CUSTOMERS_BUTTON).click()

    @allure.step("Найти клиента по имени: {first_name}")
    def find_customer_by_name(self, first_name):
        self.find_element(ManagerPageLocators.SEARCH_INPUT).send_keys(first_name)
        self.find_element(ManagerPageLocators.CUSTOMERS_TABLE)

    @allure.step("Получить данные клиента из последней строки таблицы")
    def get_customer_data_from_row(self):
        # Переходим на вкладку с таблицей
        self.go_to_customers_tab()
        # Ждём появления хотя бы одной строки
        WebDriverWait(self.driver, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr"))
        )
        # берём ПОСЛЕДНЮЮ строку — новый клиент добавляется в конец
        last_row = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")[-1]
        cells = last_row.find_elements(By.CSS_SELECTOR, "td")

        first_name = cells[0].text
        last_name = cells[1].text
        post_code = cells[2].text

        return {"first_name": first_name, "last_name": last_name, "post_code": post_code}

    @allure.step("Нажать на заголовок 'First Name' для сортировки")
    def sort_by_first_name(self):
        self.find_element(ManagerPageLocators.FIRST_NAME_HEADER).click()

    @allure.step("Получить список имен клиентов из таблицы")
    def get_customer_first_names(self):
        self.find_element(ManagerPageLocators.CUSTOMERS_TABLE)
        name_cells = self.find_elements(ManagerPageLocators.ALL_FIRST_NAME)
        return [cell.text for cell in name_cells]

    @allure.step("Удалить клиента с именем: {customer_name}")
    def delete_customer(self, customer_name):
        customer_row = self.find_element(
            ManagerPageLocators.customer_row_by_text(customer_name)
        )
        delete_btn = customer_row.find_element(
            By.CSS_SELECTOR, "button[ng-click^='deleteCust']"
        )
        delete_btn.click()
