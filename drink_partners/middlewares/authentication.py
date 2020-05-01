import json

from aiohttp import web
from aiohttp.web import Response
from aiohttp.web_exceptions import HTTPError, HTTPUnauthorized

from drink_partners.backends.pools.authentication import (
    AuthenticationBackendPool
)

ROUTES_TO_IGNORE = (
    '/healthcheck/',
)


async def test_handler(request):
    return Response(text='I am a handler.')


@web.middleware
async def authentication_middleware(request, handler):
    if (
        hasattr(request, 'match_info') and
        request.match_info.http_exception is not None and
        isinstance(request.match_info.http_exception, HTTPError)
    ):
        return (await handler(request))

    if request.url.path.startswith(ROUTES_TO_IGNORE):
        return (await handler(request))

    backend = AuthenticationBackendPool.get_default()
    application = await backend.authenticate(request=request)

    if not application:
        return HTTPUnauthorized(
            text=json.dumps({'error_message': 'Invalid authentication.'})
        )

    request.application = application

    return (await handler(request))
