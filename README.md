# Simbirsoft_intensive

UI автотесты на создание клиента, удаление клиента и сортировку списка клиентов по имени.

API автотесты на отправку GET, POST, PATCH, DELETE запросов.

В проекте используются Python 3.10, Selenium, Pytest, Requests, Pydantic 

Реализована возможность параллельного запуска тестов с помощью pytest-xdist.

Выполнен отчет о тестировании с помощью Allure.

UI тестирование проводится в браузере Chrome версии 128.0.6613.85.




## Установка и запуск

1. Склонировать репозиторий:
```commandline
git clone 'using the web URL'
```
2. Перейти в директорию проекта
3. Создать виртуальное окружение:
```commandline
python -m venv venv
```
4. Активировать виртуальное окружение:
```commandline
venv\Scripts\activate.bat
```
5. Установить зависимости:
```commandline
pip install -r requirements.txt
```
6. Запустить UI тесты:
```commandline
pytest -m Ui --alluredir=allure-results
```
Запустить API тесты:
```commandline
pytest -m Api --alluredir=allure-results
```
7. Посмотреть сгенерированный allure отчет:
```commandline
allure serve ./allure-results
```