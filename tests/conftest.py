import pytest
from fastapi.testclient import TestClient

from main import get_app


@pytest.fixture(scope="function")
def client():
    """
    Returns one instance of 'app'.
    """
    return TestClient(get_app())
