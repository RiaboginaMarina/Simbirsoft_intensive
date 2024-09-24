from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from data.config import WAIT_TIMEOUT


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator):
        return wait(self.browser, WAIT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        return wait(self.browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        return wait(self.browser, WAIT_TIMEOUT).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return wait(self.browser, WAIT_TIMEOUT).until(EC.presence_of_all_elements_located(locator))

    def switch_to_alert(self):
        return self.browser.switch_to.alert
