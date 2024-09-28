import allure
import pytest

from lib.service_api import get_entity, create_entity_and_get_id, get_all_entities, delete_entity, update_entity


@allure.story("API")
@allure.title("Создание сущности")
@allure.description(
    """
    Цель: 
        Проверить создание сущности /api/create
    
    Шаги:
        1. Создать сущность 
        2. Проверить создание сущности
    
    Постусловие:
        - Удалить созданную сущность
    
    Ожидаемый результат:
        - Сущность создана
    
    """
)
@pytest.mark.Api
def test_create_entity(api_client, test_entity):
    with allure.step("Создать сущность"):
        entity_id = create_entity_and_get_id(api_client, test_entity.model_dump())

    with allure.step("Проверить создание сущности"):
        assert entity_id == get_entity(api_client, entity_id)["id"], "Сущность не была создана"

    with allure.step("Удаление сущности"):
        delete_entity(api_client, entity_id)


@allure.story("API")
@allure.title("Получение списка сущностей")
@allure.description(
    """
    Цель:
        Проверить получение списка всех сущностей /api/getAll
        
    Предусловие:
        - Создать сущность    

    Шаги:
        1. Получить список сущностей
        2. Проверить получение списка сущностей

    Постусловие:
        - Удалить созданную сущность

    Ожидаемый результат:
        - Список сущностей получен

    """
)
@pytest.mark.Api
def test_get_all_entities(api_client, temp_entity):
    with allure.step("Получить список сущностей"):
        response = get_all_entities(api_client)

    with allure.step("Проверить получение списка"):
        assert len(response) > 0, "Список сущностей не получен"


@allure.story("API")
@allure.title("Получение сущности")
@allure.description(
    """
    Цель:
        Проверить получение сущности по id /api/get/{id}
        
    Предусловие:
        - Создать сущность     

    Шаги:
        1. Получить сущность по id
        2. Проверить получение сущности

    Постусловие:
        - Удалить созданную сущность

    Ожидаемый результат:
        - Сущность получена

    """
)
@pytest.mark.Api
def test_get_entity(api_client, temp_entity):
    with allure.step("Получить сущность по id"):
        response = get_entity(api_client, temp_entity.id)

    with allure.step("Проверить получение сущности"):
        assert len(response) > 0, "Сущность не была получена"


@allure.story("API")
@allure.title("Обновление данных сущности")
@allure.description(
    """
    Цель:
        Проверить обновление данных сущности /api/patch/{id}
        
    Предусловие:
        - Создать сущность     

    Шаги:
        1. Обновить поле 'title' сущности
        2. Проверить обновление данных в поле 'title'

    Постусловие:
        - Удалить созданную сущность

    Ожидаемый результат:
        - Данные в поле 'title' обновлены

    """
)
@pytest.mark.Api
def test_update_entity(api_client, temp_entity):
    with allure.step("Обновить поле 'title' сущности"):
        temp_entity.title = "Новое название"
        update_entity(api_client, temp_entity.id, temp_entity.model_dump())

    with allure.step("Проверить обновление данных поля 'title' сущности"):
        new_entity = get_entity(api_client, temp_entity.id)
        assert new_entity.get("title") == temp_entity.title, "Данные сущности не обновились"


@allure.story("API")
@allure.title("Удаление сущности")
@allure.description(
    """
    Цель:
        Проверить удаление сущности /api/delete/{id}
        
    Предусловие:
        - Создать сущность     

    Шаги: 
        1. Удалить созданную сущность по id
        2. Проверить удаление сущности

    Ожидаемый результат:
        - Сущность удалена

    """
)
@pytest.mark.Api
def test_delete_entity(api_client, created_entity):
    with allure.step("Удалить сущность по id"):
        delete_entity(api_client, created_entity.id)

    with allure.step("Проверить удаление сущности"):
        all_entities = get_all_entities(api_client)
        assert all(entity.get("id") != created_entity.id for entity in all_entities["entity"]), "Сущность не была удалена"
