from selenium.webdriver.common.by import By

class ManagerPageLocators:
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
    OPEN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[ng-click='openAccount()']")
    CUSTOMERS_BUTTON = (By.CSS_SELECTOR, "button[ng-click='showCust()']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

class CustomersLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[ng-model='searchCustomer']")
    CUSTOMERS_TABLE = (By.CSS_SELECTOR, "table.table")
    TABLE_ROWS = (By.CSS_SELECTOR, "table.table tbody tr")
    HEADER_FIRST_NAME = (By.XPATH, "//table//th[.='First Name']")
    CELL_FIRST_NAME = (By.CSS_SELECTOR, "td:nth-child(1)")
    CELL_LAST_NAME = (By.CSS_SELECTOR, "td:nth-child(2)")
    CELL_POST_CODE = (By.CSS_SELECTOR, "td:nth-child(3)")
    CELL_DELETE_BTN = (By.CSS_SELECTOR, "td:last-child button")