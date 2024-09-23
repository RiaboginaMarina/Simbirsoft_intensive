from data.config import BASE_URL
from pages.base_page import BasePage
from pages.locators import AllLocators


class ManagerPage(BasePage):
    URL = BASE_URL + "manager"

    def __init__(self, browser, url=URL):
        super().__init__(browser, url)

    def open_add_customers_form(self):
        self.element_is_clickable(AllLocators.ADD_CUSTOMER_OPEN_FORM_BUTTON).click()

    def open_customers_data(self):
        self.element_is_clickable(AllLocators.CUSTOMER_BUTTON).click()

    def set_first_name(self, name):
        self.element_is_visible(AllLocators.FIRST_NAME_FIELD).send_keys(name)

    def set_last_name(self, surname):
        self.element_is_visible(AllLocators.LAST_NAME_FIELD).send_keys(surname)

    def set_post_code(self, post_code):
        self.element_is_visible(AllLocators.POST_CODE_FIELD).send_keys(post_code)

    def click_submit_form_button(self):
        self.element_is_clickable(AllLocators.ADD_CUSTOMER_SUBMIT_BUTTON).click()

    def fill_customers_form(self, name, surname, post_code):
        self.set_first_name(name)
        self.set_last_name(surname)
        self.set_post_code(post_code)

    def get_text_from_alert(self):
        return self.switch_to_alert().text

    def close_alert_window(self):
        self.switch_to_alert().accept()

    def get_text_from_table(self):
        return self.element_is_visible(AllLocators.CUSTOMERS_TABLE).text

    def sort_by_first_name(self):
        self.element_is_clickable(AllLocators.FIRST_NAME_TABLE_HEAD).click()

    def get_names_from_table(self):
        names = self.find_elements(AllLocators.FIRST_NAME_COLUMN)
        return [name.text for name in names[1:]]

    def delete_customer_by_name(self, name):
        (self.find_element(
            (AllLocators.DELETE_BUTTON[0],
             AllLocators.DELETE_BUTTON[1].format(name))).click())
