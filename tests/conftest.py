import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pytest_plugins = "tests.fixtures"


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
