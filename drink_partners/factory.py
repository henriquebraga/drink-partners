from aiohttp import web

from drink_partners.healthcheck.routes import (
    register_routes as register_healthcheck_routes
)
from drink_partners.middlewares.exception_handler import (
    exception_handler_middleware
)
from drink_partners.middlewares.version import version_middleware


def build_app(loop=None):
    app = web.Application(loop=loop, middlewares=get_middlewares())

    app.on_startup.append(start_plugins)
    app.on_cleanup.append(stop_plugins)

    register_routes(app)

    return app


def register_routes(app):  # pragma: no cover
    register_healthcheck_routes(app)


def get_middlewares():
    return [
        exception_handler_middleware,
        version_middleware
    ]


async def start_plugins(app):  # pragma: no cover
    pass


async def stop_plugins(app):  # pragma: no cover
    pass
