import pytest

from lib.modules.service_api import ServiceApi


@pytest.fixture(scope="session")
def api_client():
    return ServiceApi()
