import random
import string
import time

import allure
import pytest

from pages.manager_page import ManagerPage


def generate_random_number(length):
    rand_number = ''
    for i in range(length):
        rand_number += str(random.randint(0, 9))
    return rand_number


def create_word_from_number(number):
    alphabet = string.ascii_lowercase
    word = ''
    while number:

        letter_number = int(number[:2])
        word += alphabet[letter_number % 26]
        number = number[2:]
    return word


def generate_random_word(length):
    alphabet = string.ascii_lowercase
    return ''.join(random.choice(alphabet) for _ in range(length))


def convert_table_data_to_list(table_data):
    result = []
    for line in table_data.split('\n')[1:]:
        result.append(line.split())
    return result


@allure.title("Создание нового клиента")
@allure.description(
    """
    Цель: Проверить создание нового клиента
    
    Предусловие: 
        - Открыть браузер
        
    Шаги:
        1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"  
        2. Нажать кнопку Add Customer
        3. Заполнить поля First Name, Last Name, Post Code валидными данными
        4. Нажать кнопку Add Customer под формой регистрации
        5. Проверить появление уведомления об успешном создании клиента
        
    Ожидаемый результат:
        - Появилось всплывающее сообщение с текстом "Customer added successfully with customer id :" и номером id      
    """
)
@pytest.mark.parametrize("surname, post_code",
                         [
                             (generate_random_word(10),
                              generate_random_number(10))
                         ])
def test_add_customer_successfully(browser, surname, post_code):

    with allure.step("Открытие страницы https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"):
        page = ManagerPage(browser)
        page.open()
        page.wait_for_page_load()

    with allure.step("Открытие формы создания клиента"):
        page.open_add_customers_form()
        time.sleep(3)

    with allure.step("Заполнение формы создания нового клиента"):
        name = create_word_from_number(post_code)
        page.fill_customers_form(name, surname, post_code)
        page.click_submit_form_button()

    with allure.step("Проверка появления всплывающего уведомления"):
        expected_alert_text = "Customer added successfully with customer id :"
        actual_alert_text = page.get_text_from_alert_window()
        assert expected_alert_text in actual_alert_text, "Текст об успешном создании клиента не найден"


@allure.title("Сортировка списка клиентов по имени")
@allure.description(
    """
    Цель: Проверить сортировку списка клиентов по имени
    
    Предусловие:
        - Открыть браузер
    
    Шаги:
        1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"  
        2. Нажать кнопку Customers
        3. Кликнуть один раз на заголовок столбца First Name
        4. Проверить сортировку имен в алфавитном порядке по убыванию
        
    Ожидаемый результат:
        - Клиенты отсортировались по имени     
    """
)
def test_alphabet_order(browser):

    with allure.step("Открытие страницы https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"):
        page = ManagerPage(browser)
        page.open()
        page.wait_for_page_load()

    with allure.step("Открытие списка клиентов"):
        page.open_customers_data()
        time.sleep(2)

    with allure.step("Получение несортированных данных из таблицы"):
        unsorted_table = convert_table_data_to_list(page.get_text_from_table())

    with allure.step("Сортировка клиентов по имени"):
        page.sort_by_first_name()

    with allure.step("Проверка сортировки списка клиентов по имени"):
        expected_sorted_table = sorted(unsorted_table, reverse=True, key=lambda i: i[0])
        actual_sorted_table = convert_table_data_to_list(page.get_text_from_table())
        assert expected_sorted_table == actual_sorted_table, "Данные не отсортировались по столбцу first name"


@allure.title("Удаление клиента")
@allure.description(
    """
    Цель: Проверить удаление клиента

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"  
        2. Нажать кнопку Customers
        3. Найти нужного клиента по имени
        4. Нажать кнопку Delete в строке с нужным именем клиента
        5. Проверить удаление клиента из таблицы

    Ожидаемый результат:
        - Клиент удален из таблицы Customers     
    """
)
def test_delete_client_successfully(browser):

    with allure.step("Открытие страницы https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"):
        page = ManagerPage(browser)
        page.open()
        page.wait_for_page_load()

    with allure.step("Открытие списка клиентов"):
        page.open_customers_data()
        time.sleep(2)

    with allure.step("Нахождение имени клиента для удаления"):
        name_list = page.get_names_from_table()
        avg_name_length = sum(map(len, name_list)) // len(name_list)
        name_list_sorted = sorted(name_list, key=len)
        name_to_delete = name_list_sorted[len(name_list_sorted) // 2 - 1]

    with allure.step("Удаление клиента"):
        page.delete_customer_by_name(name_to_delete)

    with allure.step("Проверка удаления клиента из таблицы"):
        name_list_after_deleting = page.get_names_from_table()
        assert name_to_delete not in name_list_after_deleting, "Пользователь не удален"
