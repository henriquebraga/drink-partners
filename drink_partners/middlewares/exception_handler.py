from aiohttp import web

from drink_partners.contrib.exceptions import APIException
from drink_partners.contrib.response import JSONResponse


@web.middleware
async def exception_handler_middleware(request, handler):

    try:
        return await handler(request)

    except APIException as exc:
        return JSONResponse(data=exc.as_dict(), status=exc.status_code)

    except web.HTTPError as exc:
        data = {'error_code': 'unexpected_error', 'error_message': exc.reason}
        return JSONResponse(data=data, status=exc.status_code)

    except Exception:
        data = {
            'error_code': 'unexpected_error',
            'error_message': 'Internal server error'
        }
        return JSONResponse(data=data, status=500)
