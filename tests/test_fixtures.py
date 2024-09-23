import pytest

from common.utils import generate_random_number, generate_random_word


@pytest.fixture
def rand_post_code():
    return generate_random_number(10)


@pytest.fixture
def rand_surname():
    return generate_random_word(10)
