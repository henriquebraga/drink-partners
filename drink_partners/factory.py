from aiohttp import web


def build_app(loop=None):
    app = web.Application(loop=loop, middlewares=get_middlewares())

    app.on_startup.append(start_plugins)
    app.on_cleanup.append(stop_plugins)

    register_routes(app)

    return app


def register_routes(app):
    pass


def get_middlewares():
    return []


async def start_plugins(app):
    pass


async def stop_plugins(app):
    pass
