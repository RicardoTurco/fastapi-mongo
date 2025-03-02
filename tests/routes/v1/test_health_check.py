import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_health_check_success(client):
    """
    Test: test_health_check_success.
    """
    response = client.get("/v1/health-check")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"application": True}
