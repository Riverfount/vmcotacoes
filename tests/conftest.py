import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from rates.app import app


@pytest_asyncio.fixture
async def client():
    """This fixture provide an async test client to do all the requests to the fastAPI endpoints."""
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url='http://test', follow_redirects=True) as ac:
            yield ac
