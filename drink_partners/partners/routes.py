from drink_partners.partners.views.partner_create_view import PartnerCreateView
from drink_partners.partners.views.partner_get_view import PartnerGetView


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
