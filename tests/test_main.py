import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_ok(client: AsyncClient):
    response = await client.get('/health')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'The Api is 100% healthy.'}
