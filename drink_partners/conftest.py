import asyncio

import pytest

from drink_partners import app as _app


@pytest.fixture(scope='session')
def loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def app(loop):
    return _app


@pytest.fixture(autouse=True)
async def client(aiohttp_client, app):
    return await aiohttp_client(app)
