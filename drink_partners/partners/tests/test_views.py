import pytest


class TestPartnerGetView:

    @pytest.fixture
    def url(self):
        return '/partner/1/'

    @pytest.fixture
    def partner_with_str_id_url(self):
        return '/partner/id-str/'

    @pytest.fixture
    def partner_not_found_url(self):
        return '/partner/100/'

    async def test_get_should_return_partner(
        self,
        client,
        url,
        save_partner
    ):
        async with client.get(url) as response:
            assert response.status == 200
            partner = await response.json()
            del save_partner['_id']
            assert partner == save_partner

    async def test_get_should_return_bad_request_when_id_is_str(
        self,
        client,
        partner_with_str_id_url,
        save_partner
    ):
        async with client.get(partner_with_str_id_url) as response:
            assert response.status == 400
            content = await response.json()
            assert content['error_code'] == 'bad_request'

            details = content['error_message']

            assert details == 'Partner id "id-str" must be an integer value'

    async def test_get_should_return_not_found_when_partner_does_not_exist(
        self,
        client,
        partner_not_found_url,
        save_partner
    ):
        async with client.get(partner_not_found_url) as response:
            assert response.status == 404
            content = await response.json()
            assert content['error_code'] == 'not_found'

            details = content['error_message']

            assert details == 'Partner not found for id: 100'
