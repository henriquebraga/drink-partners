import json
import logging

from aiohttp import web

from drink_partners.backends.pools.partners import PartnersBackendPool
from drink_partners.contrib.exceptions import BadRequest, NotFound
from drink_partners.contrib.response import JSONResponse

logger = logging.getLogger(__name__)


class PartnerGetView(web.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.datasource = PartnersBackendPool.get_default()

    async def get(self):
        _id = self.request.match_info.get('id')

        partner = await self._get_partner(_id)

        if not partner:
            logger.warning(f'Partner not found for id: {_id}')
            raise NotFound(
                error_message=f'Partner not found for id: {_id}'
            )

        return JSONResponse(data=json.dumps(partner))

    async def _get_partner(self, _id):
        try:
            return await self.datasource.get_by_id(_id)
        except ValueError:
            logger.warning(f'Partner id "{_id}" must be an integer value')

            raise BadRequest(
                error_message=f'Partner id "{_id}" must be an integer value'
            )
