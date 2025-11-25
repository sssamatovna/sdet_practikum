from selenium.webdriver.common.by import By


class ManagerLocators:
    """Локаторы для общей страницы менеджера и вкладки 'Add Customer'."""
    ADD_CUSTOMER_TAB = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
    CUSTOMERS_TAB = (By.CSS_SELECTOR, "button[ng-click='showCust()']")

    # Элементы вкладки Add Customer
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    ADD_CUSTOMER_BTN = (By.CSS_SELECTOR, "button[type='submit']")


class CustomersLocators:
    CUSTOMER_TABLE_ROWS = (By.XPATH, "//table[contains(@class, 'table-striped')]/tbody/tr")
    SORT_BY_FNAME_LINK = (By.XPATH, "//a[contains(text(), 'First Name')]")
    # Локатор для всех ячеек с именами
    FNAME_CELLS = (By.XPATH, "//table[contains(@class, 'table-striped')]/tbody/tr/td[1]")
