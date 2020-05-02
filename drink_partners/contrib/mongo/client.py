import asyncio
import logging

from motor.motor_asyncio import AsyncIOMotorClient
from simple_settings import settings

from drink_partners.contrib.models.singleton import SingletonMixin

logger = logging.getLogger(__name__)


class MongoClient(SingletonMixin):

    def __init__(self):
        logger.info(
            f'Connection to the mongodb: {settings.MOTOR_URI} '
            f'with pool size: {settings.MOTOR_MAX_POOL_SIZE}'
        )
        self._client = AsyncIOMotorClient(
            settings.MOTOR_URI,
            maxPoolSize=settings.MOTOR_MAX_POOL_SIZE,
            io_loop=asyncio.get_event_loop(),
            **settings.MOTOR_KWARGS
        )
        logger.info(f'Default mongodb database: {self.db.name}')

    @property
    def db(self):
        return self._client.get_database(settings.MOTOR_DB)

    def get_collection(self, name):
        return self.db.get_collection(name)

    def close(self):
        logger.info('Closing mongodb connection')
        if self._client:
            self._client.close()
            self._client = None
