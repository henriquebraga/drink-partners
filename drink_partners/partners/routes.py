from .views import PartnerCreateView, PartnerGetView


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
