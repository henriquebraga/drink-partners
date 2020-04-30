import pytest

from drink_partners.extensions.authentication.static import (
    StaticAuthenticationBackend
)


class TestStaticAuthentication:

    @pytest.fixture
    def backend(self):
        return StaticAuthenticationBackend.create()

    async def test_respects_the_token_from_querystring_param(
        self,
        backend,
        make_request,
        token,
        application,
        settings_with_applications
    ):
        request = make_request(
            method='get',
            url='https://www.zedelivery.com.br/',
            params={'token': token}
        )

        authorized_application = await backend.authenticate(request)

        assert application['name'] == authorized_application['name']

    async def test_respects_the_token_from_headers(
        self,
        backend,
        make_request,
        token,
        application,
        settings_with_applications
    ):
        request = make_request(
            method='get',
            url='https://www.zedelivery.com.br/',
            headers={backend.AUTH_HEADER: token}
        )

        authorized_application = await backend.authenticate(request)

        assert application['name'] == authorized_application['name']

    async def test_returns_none_for_non_authenticated_request(
        self,
        backend,
        make_request,
        settings_with_applications
    ):
        request = make_request(
            method='get',
            url='https://www.zedelivery.com.br/'
        )

        application = await backend.authenticate(request)
        assert application is None
