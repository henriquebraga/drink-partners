from ramos.mixins import SingletonCreateMixin

from drink_partners.backends.partners.backend import PartnersBackend
from drink_partners.contrib.mongo.client import MongoClient


class PartnersMongoDbBackend(SingletonCreateMixin, PartnersBackend):
    id = 'mongodb'
    name = 'MongoDB partners datasource'

    @property
    def partners_collection(self):
        return MongoClient().get_collection('partners')

    async def get_by_id(self, _id):
        return await self.partners_collection.find_one(
            {'id': int(_id)}, {'_id': 0}
        )
