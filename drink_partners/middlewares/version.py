from aiohttp import web

from drink_partners.version import __version__


@web.middleware
async def version_middleware(request, handler):
    response = await handler(request)
    response.headers['X-API-Version'] = __version__
    return response
