import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from simple_settings import settings

from drink_partners.contrib.models.singleton import SingletonMixin


class MongoClient(SingletonMixin):

    def __init__(self, loop=None):

        if not loop:
            loop = asyncio.get_event_loop()

        self._client = AsyncIOMotorClient(
            settings.MOTOR_URI,
            maxPoolSize=settings.MOTOR_MAX_POOL_SIZE,
            io_loop=loop,
            **settings.MOTOR_KWARGS
        )

    @property
    def db(self):
        return self._client.get_database(settings.MOTOR_DB)

    def get_collection(self, name):
        return self.db.get_collection(name)

    def close(self):
        if self._client:
            self._client.close()
            self._client = None
