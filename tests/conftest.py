from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.test_fixtures import *


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
