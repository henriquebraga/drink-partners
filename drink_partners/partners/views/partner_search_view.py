import json
import logging

from geojson import Point

from drink_partners.contrib.exceptions import BadRequest, NotFound
from drink_partners.contrib.response import JSONResponse
from drink_partners.partners.views.generic import PartnerView

logger = logging.getLogger(__name__)


class PartnerLatLongSearchView(PartnerView):

    async def get(self):
        lng = self.request.match_info.get('lng')
        lat = self.request.match_info.get('lat')

        coordinate = self._get_coordinate(lng, lat)

        partner = await self._search_nearest_partner_by_coordinate(coordinate)

        return JSONResponse(data=json.dumps(partner))

    def _get_coordinate(self, lng, lat):
        error_message = f'Invalid coordinate longitude:{lng} latitude:{lat}'
        coordinate = [0, 0]
        try:
            coordinate = Point((float(lng), float(lat)))
        except Exception:
            raise BadRequest(
                error_message=error_message
            )

        return coordinate

    async def _search_nearest_partner_by_coordinate(self, coordinate):
        partner = await self.datasource.search_nearest_by_coordinate(
            coordinate
        )

        lng, lat = coordinate['coordinates']

        if not partner:
            error_message = (
                f'Partners not found covering area '
                f'for latitude:{lng} longitude:{lat}'
            )
            raise NotFound(
                error_message=error_message
            )

        return partner
