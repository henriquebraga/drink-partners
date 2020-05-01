from .views import PartnerGetView


def register_routes(app):
    app.router.add_route(
        'GET',
        '/partner/{id}/',
        PartnerGetView
    )
