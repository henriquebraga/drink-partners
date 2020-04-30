from drink_partners.version import __version__


class TestVersionMiddleware:

    async def test_version_middleware(self, client):
        async with client.get('/healthcheck/') as response:
            assert response.status == 200
            assert response.headers.get('X-API-Version') == __version__
