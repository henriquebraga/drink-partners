from drink_partners.contrib.samples import partner_bar_legal


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

    async def test_should_return_nearest_partner_for_coordinate(
        self,
        client,
        partner_search_coordinates_url,
        save_partners
    ):
        async with client.get(partner_search_coordinates_url) as response: # noqa
            assert response.status == 200

            response_json = await response.json()

            assert response_json == partner_bar_legal()

    async def test_should_return_not_found_when_no_partner_covers_coordinate(
        self,
        client,
        partner_search_coordinates_url
    ):
        async with client.get(partner_search_coordinates_url) as response: # noqa
            assert response.status == 404

            response_json = await response.json()

            assert response_json['error_code'] == 'not_found'

            assert response_json['error_message'] == (
                'Partners not found covering area for '
                'latitude:-43.36556 longitude:-22.99669'
            )
