from pages.locators import AllLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class ManagerPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    def open(self):
        self.browser.get(self.url)

    def wait_for_page_load(self):
        try:
            element_present = EC.visibility_of_element_located((By.XPATH, "//button[@ng-class='btnClass1']"))
            WebDriverWait(self.browser, 5).until(element_present)
        except TimeoutException:
            print("Ожидание загрузки страницы истекло")

    def open_add_customers_form(self):
        self.browser.find_element(*AllLocators.ADD_CUSTOMER_OPEN_FORM_BUTTON).click()

    def open_customers_data(self):
        self.browser.find_element(*AllLocators.CUSTOMER_BUTTON).click()

    def set_first_name(self, name):
        name_input = self.browser.find_element(*AllLocators.FIRST_NAME_FIELD)
        name_input.send_keys(name)

    def set_last_name(self, surname):
        surname_input = self.browser.find_element(*AllLocators.LAST_NAME_FIELD)
        surname_input.send_keys(surname)

    def set_post_code(self, post_code):
        post_code_input = self.browser.find_element(*AllLocators.POST_CODE_FIELD)
        post_code_input.send_keys(post_code)

    def click_submit_form_button(self):
        self.browser.find_element(*AllLocators.ADD_CUSTOMER_SUBMIT_BUTTON).click()

    def fill_customers_form(self, name, surname, post_code):
        self.set_first_name(name)
        self.set_last_name(surname)
        self.set_post_code(post_code)

    def get_text_from_alert_window(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        return alert_text

    def get_text_from_table(self):
        return self.browser.find_element(*AllLocators.CUSTOMERS_TABLE).text

    def sort_by_first_name(self):
        self.browser.find_element(*AllLocators.FIRST_NAME_TABLE_HEAD).click()

    def get_names_from_table(self):
        name_list = []
        names = self.browser.find_elements(*AllLocators.FIRST_NAME_COLUMN)
        for name in names:
            name_list.append(name.text)
        return name_list[1:]

    def delete_customer_by_name(self, name):
        (self.browser.find_element(
            AllLocators.DELETE_BUTTON[0],
            AllLocators.DELETE_BUTTON[1].format(name)).click())



