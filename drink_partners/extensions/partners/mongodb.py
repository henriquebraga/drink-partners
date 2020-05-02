from ramos.mixins import SingletonCreateMixin

from drink_partners.backends.partners.backend import PartnersBackend
from drink_partners.contrib.exceptions import PartnerAlreadyExists
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

    async def get_by_document(self, document):
        return await self.partners_collection.find_one(
            {'document': document}, {'_id': 0}
        )

    async def save(self, payload):
        partner = await self.get_by_document(payload['document'])

        if partner:
            raise PartnerAlreadyExists(
                partner_id=payload['id'],
                document=payload['document']
            )

        await self.partners_collection.insert_one(payload)
        del payload['_id']
