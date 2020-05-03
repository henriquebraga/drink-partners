from ramos.mixins import SingletonCreateMixin

from drink_partners.backends.partners.backend import PartnersBackend
from drink_partners.contrib.exceptions import PartnerAlreadyExists
from drink_partners.contrib.mongo.client import MongoClient
from drink_partners.contrib.utils.points_distance import (
    get_coordinate_distance_points
)


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

        payload['id'] = int(payload['id'])
        await self.partners_collection.insert_one(payload)
        del payload['_id']

    async def search_nearest_by_lng_lat(self, coordinate):
        criteria = {
            'coverageArea': {
                '$geoIntersects': {
                    '$geometry': coordinate
                }
            }
        }

        cursor = self.partners_collection.find(criteria, {'_id': 0})
        partners = [
            self._set_distance_between_destiny_and_partner(
                partner=data,
                destiny=coordinate
            )
            async for data in cursor
        ]
        if not partners:
            return None

        nearest_partner = min(partners, key=lambda p: p['distance'])

        del nearest_partner['distance']

        return nearest_partner

    def _set_distance_between_destiny_and_partner(self, partner, destiny):
        partner['distance'] = get_coordinate_distance_points(
            partner['address']['coordinates'],
            destiny['coordinates']
        )
        return partner
