class TestPartnerGetView:

    async def test_get_should_return_partner(
        self,
        client,
        url,
        save_partner
    ):
        async with client.get(url) as response:
            assert response.status == 200
            partner = await response.json()
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


class TestProductCreateView:

    async def test_should_return_status_ok(
        self,
        client,
        create_partner_url,
        create_partner_payload,
    ):
        async with client.post(
            create_partner_url,
            json=create_partner_payload
        ) as response:
            assert response.status == 201

    async def test_should_return_bad_request_when_no_payload(
        self,
        client,
        create_partner_url,
        create_partner_payload,
    ):
        async with client.post(
            create_partner_url,
            json=None
        ) as response:
            assert response.status == 400
