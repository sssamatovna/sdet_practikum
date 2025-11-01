from selenium.webdriver.common.by import By

class ManagerPageLocators:

    # главные элементы
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
    CUSTOMERS_BUTTON = (By.CSS_SELECTOR, "button[ng-click='showCust()']")
    FIRST_NAME_HEADER = (By.CSS_SELECTOR, "a[ng-click*='fName']")

    # форма
    FIRST_NAME = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # таблица
    CUSTOMERS_TABLE = (By.CSS_SELECTOR, "table.table-striped")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[ng-model='searchCustomer']")
    ALL_FIRST_NAME = (By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
    ALL_LAST_NAME = (By.CSS_SELECTOR, "tbody tr td:nth-child(2)")
    ALL_POST_CODE = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")

    @staticmethod
    def customer_row_by_text(text):
        return By.XPATH, f"//tr[contains(., '{text}')]"