from aiohttp.web import Response

from drink_partners.middlewares.authentication import (
    ROUTES_TO_IGNORE,
    authentication_middleware
)


async def test_handler(request):
    return Response(text='I am a handler.')


class TestAuthMiddleware:

    async def test_returns_application_for_authorized_request(
        self,
        make_request,
        application,
        token,
        settings_with_applications
    ):
        request = make_request(
            method='get',
            url='https://www.zedelivery.com.br/',
            params={'token': token}
        )

        response = await authentication_middleware(
            request=request,
            handler=test_handler
        )

        assert response.status == 200
        assert request.application == application

    async def test_returns_401_for_unauthorized_request(
        self,
        make_request
    ):
        request = make_request(
            method='get',
            url='https://www.zedelivery.com.br/'
        )

        response = await authentication_middleware(
            request=request,
            handler=test_handler
        )

        assert response.status == 401

    async def test_ignores_route(
        self,
        make_request
    ):
        request = make_request(
            method='get',
            url=f'https://www.zedelivery.com.br{ROUTES_TO_IGNORE[0]}'
        )

        response = await authentication_middleware(
            request=request,
            handler=test_handler
        )

        assert response.status == 200

    async def test_should_ignore_previous_errors_raised(
        self,
        client
    ):
        async with client.get(
            '/foo/',
            headers={'Authorization': 'talkei'}
        ) as response:
            assert response.status == 404
