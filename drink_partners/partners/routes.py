from drink_partners.partners.views.partner_create_view import PartnerCreateView
from drink_partners.partners.views.partner_get_view import PartnerGetView
from drink_partners.partners.views.partner_search_view import (
    PartnerLatLongSearchView
)


def register_routes(app):
    app.router.add_route(
        'GET',
        '/partner/{id}/',
        PartnerGetView
    )

    app.router.add_route(
        'POST',
        '/partner/',
        PartnerCreateView
    )

    app.router.add_route(
        'GET',
        '/partner/search/lng/{lng}/lat/{lat}/',
        PartnerLatLongSearchView
    )
