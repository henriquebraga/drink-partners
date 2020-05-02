import asyncio

import pytest
from aiohttp.client_reqrep import ClientRequest
from simple_settings.utils import settings_stub
from yarl import URL

from drink_partners import app as _app
from drink_partners.contrib.mongo.client import MongoClient


@pytest.fixture(scope='session')
def loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
def mongo_database():
    return MongoClient()


@pytest.fixture(autouse=True)
async def clean_database(mongo_database):
    collections_name = await mongo_database.db.list_collection_names()

    [
        mongo_database.db.drop_collection(c)
        for c in collections_name
        if not c.startswith('system')
    ]


@pytest.fixture
def app(loop):
    return _app


@pytest.fixture
def application():
    return {'name': 'test', 'active': True}


@pytest.fixture
def token():
    return 'token'


@pytest.fixture
def settings_with_applications(token):
    applications_settings = {
        'test': token
    }

    with settings_stub(
        AUTH_APPLICATIONS=applications_settings
    ) as mocked_settings:
        yield mocked_settings


@pytest.fixture(autouse=True)
async def client(aiohttp_client, token, settings_with_applications, app):
    return await aiohttp_client(app, headers={'Authorization': token})


@pytest.fixture
async def make_request(loop):
    """
    Inspired on aiohttp make-request function
    https://github.com/aio-libs/aiohttp/blob/master/tests/test_client_request.py#L24
    """
    request = None

    def maker(method, url, *args, **kwargs):
        nonlocal request
        request = ClientRequest(method, URL(url), *args, loop=loop, **kwargs)
        return request

    yield maker
    if request is not None:
        await request.close()
