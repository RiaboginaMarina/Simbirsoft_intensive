from typing import Dict

from requests import Response

from api_core.req import Session as req
from lib.modules.service_api import ServiceApi


def create_entity_and_get_id(client: ServiceApi, body: Dict):
    response: Response = client.sa_create_entity(json=body)
    print("response:", response.json(), response.text, response.content)
    assert response.status_code == req.OK, "Сущность не была создана"
    return response.json()


def get_all_entities(client: ServiceApi):
    response: Response = client.sa_get_all_entities()
    assert response.status_code == req.OK, "Не удалось получить список сущностей"
    return response.json()


def get_entity(client: ServiceApi, entity_id):
    response: Response = client.sa_get_entity(entity_id)
    assert response.status_code == req.OK, "Не удалось получить сущность"
    return response.json()


def delete_entity(client: ServiceApi, entity_id):
    response: Response = client.sa_delete_entity(entity_id)
    assert response.status_code == req.NO_CONTENT, "Сущность не была удалена"


def update_entity(client: ServiceApi, entity_id, body: Dict):
    response: Response = client.sa_update_entity(entity_id, json=body)
    assert response.status_code == req.NO_CONTENT, "Не удалось обновить сущность"
