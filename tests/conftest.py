import pytest


@pytest.fixture(scope="session")
def custom_fixture():
    return list(range(1, 11))
