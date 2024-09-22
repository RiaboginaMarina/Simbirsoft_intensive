import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common.utils import generate_random_number, generate_random_word


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def rand_num():
    return generate_random_number(10)


@pytest.fixture
def rand_str():
    return generate_random_word(10)
