import json
import logging

from drink_partners.contrib.exceptions import (
    BadRequest,
    Conflict,
    PartnerAlreadyExists
)
from drink_partners.contrib.response import JSONResponse
from drink_partners.partners.schemas import PartnerSchema
from drink_partners.partners.views.generic import PartnerView

logger = logging.getLogger(__name__)


class PartnerCreateView(PartnerView):

    async def post(self):
        partner = await self._validate_data()

        try:
            await self._save_partner(partner)
        except PartnerAlreadyExists as error:
            logger.warning(str(error))
            raise Conflict(
                error_message=str(error)
            )
        return JSONResponse(status=201, data=json.dumps(partner))

    async def _validate_data(self):
        data = {}

        try:
            data = await self.request.json()
        except Exception as e:
            raise BadRequest(
                error_message=f'Invalid payload: {data} error: {e}'
            )

        if not data:
            raise BadRequest(
                error_message=f'Empty JSON payload: {data}'
            )

        errors = self._validate_partner_fields(data)

        if errors:
            raise BadRequest(
                error_message=f'Invalid partner payload: {errors}'
            )

        return data

    def _validate_partner_fields(self, partner):
        schema = PartnerSchema()
        return schema.validate(partner)

    async def _save_partner(self, partner):
        await self.datasource.save(partner)
