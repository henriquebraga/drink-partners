import logging

from geojson import Point

from drink_partners.contrib.exceptions import BadRequest
from drink_partners.contrib.response import JSONResponse

from .generic import PartnerView

logger = logging.getLogger(__name__)


class PartnerLatLongSearchView(PartnerView):

    async def get(self):
        lng = self.request.match_info.get('lng')
        lat = self.request.match_info.get('lat')

        self._get_coordinate(lng, lat)

        return JSONResponse()

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
