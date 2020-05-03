class TestSearchPartner:

    async def test_should_return_bad_request_for_str_coordinates(
        self,
        client,
        partner_search_with_str_coordinates_url
    ):
        async with client.get(partner_search_with_str_coordinates_url) as response: # noqa
            assert response.status == 400

            response_json = await response.json()

            assert response_json['error_code'] == 'bad_request'
            assert response_json['error_message'] == (
                'Invalid coordinate longitude:a latitude:a'
            )

    async def test_should_return_status_ok(
        self,
        client,
        partner_search_coordinates_url
    ):
        async with client.get(partner_search_coordinates_url) as response: # noqa
            assert response.status == 200
