import json
import logging

from drink_partners.contrib.exceptions import BadRequest, NotFound
from drink_partners.contrib.response import JSONResponse
from drink_partners.partners.views.generic import PartnerView

logger = logging.getLogger(__name__)


class PartnerGetView(PartnerView):

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
            return await self.datasource.get_by_id(_id)
        except ValueError:
            logger.warning(f'Partner id "{_id}" must be an integer value')

            raise BadRequest(
                error_message=f'Partner id "{_id}" must be an integer value'
            )
