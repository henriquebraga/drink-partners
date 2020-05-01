import json

from aiohttp import web

from drink_partners.contrib.exceptions import BadRequest, NotFound
from drink_partners.contrib.mongo.client import MongoClient
from drink_partners.contrib.response import JSONResponse


class PartnerGetView(web.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.partners = MongoClient().get_collection('partners')

    async def get(self):

        _id = self.request.match_info.get('id')
        partner = await self._get_partner(_id)

        if not partner:
            raise NotFound(
                error_message=f'Partner not found for id: {_id}'
            )

        return JSONResponse(data=json.dumps(partner))

    async def _get_partner(self, _id):
        try:
            return await self.partners.find_one({'id': int(_id)}, {'_id': 0})
        except ValueError:
            raise BadRequest(
                error_message=f'Partner id "{_id}" must be an integer value'
            )
