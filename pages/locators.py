from selenium.webdriver.common.by import By


class AllLocators:
    ADD_CUSTOMER_OPEN_FORM_BUTTON = (By.XPATH, "//button[@ng-class='btnClass1']")
    CUSTOMER_BUTTON = (By.XPATH, "//button[@ng-class='btnClass3']")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@ng-model='fName']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@ng-model='lName']")
    POST_CODE_FIELD = (By.XPATH, "//input[@ng-model='postCd']")
    ADD_CUSTOMER_SUBMIT_BUTTON = (By.CLASS_NAME, "btn-default")
    CUSTOMERS_TABLE = (By.TAG_NAME, "table")
    FIRST_NAME_TABLE_HEAD = (By.XPATH, "//thead/tr/td[1]/a")
    FIRST_NAME_COLUMN = (By.XPATH, "//table//td[1]")
    DELETE_BUTTON = (By.XPATH, "//td[text()='{}']/..//button[text()='Delete']")
