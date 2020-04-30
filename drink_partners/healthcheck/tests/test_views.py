import pytest


class TestHealthCheck:

    @pytest.fixture
    def url(self):
        return '/healthcheck/'

    async def test_should_return_status_ok(self, client, url):
        async with client.get(url) as response:
            assert response.status == 200
            content = await response.json()
        assert content == {'status': 'OK'}
