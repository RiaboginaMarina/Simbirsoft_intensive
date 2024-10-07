import pytest

from data.models import Entity, Addition
from lib.service_api import create_entity_and_get_id, delete_entity


@pytest.fixture()
def created_entity(api_client, test_entity) -> Entity:
    entity_id = create_entity_and_get_id(api_client, test_entity.model_dump())
    test_entity.id = entity_id
    return test_entity


@pytest.fixture()
def temp_entity(api_client, created_entity):
    yield created_entity
    delete_entity(api_client, created_entity.id)


@pytest.fixture()
def test_entity() -> Entity:
    return Entity(addition=Addition())
