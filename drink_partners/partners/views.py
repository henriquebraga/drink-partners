import json
import logging

from aiohttp import web

from drink_partners.backends.pools.partners import PartnersBackendPool
from drink_partners.contrib.exceptions import (
    BadRequest,
    Conflict,
    NotFound,
    PartnerAlreadyExists
)
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


class PartnerCreateView(web.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.datasource = PartnersBackendPool.get_default()

    async def post(self):
        partners = await self._validate_data()

        try:
            await self._save_partners(partners)
        except PartnerAlreadyExists as error:
            logger.warning(str(error))
            raise Conflict(
                error_message=str(error)
            )
        return JSONResponse(status=201, data=json.dumps(partners))

    async def _validate_data(self):
        data = {}

        try:
            data = await self.request.json()
        except Exception as e:
            raise BadRequest(
                error_message=f'Invalid payload:{data} error:{e}'
            )

        return data.get('pdvs') or []

    async def _save_partners(self, partners):
        for partner in partners:
            await self.datasource.save(partner)
