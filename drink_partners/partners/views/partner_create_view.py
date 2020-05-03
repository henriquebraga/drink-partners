import json
import logging

from drink_partners.contrib.exceptions import (
    BadRequest,
    Conflict,
    PartnerAlreadyExists
)
from drink_partners.contrib.response import JSONResponse

from .generic import PartnerView

logger = logging.getLogger(__name__)


class PartnerCreateView(PartnerView):

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
