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

            response_json = await response.json()
            assert response_json == create_partner_payload

    async def test_should_return_bad_request_when_no_payload(
        self,
        client,
        create_partner_url
    ):
        async with client.post(
            create_partner_url,
            json=None
        ) as response:
            assert response.status == 400

            response_json = await response.json()

            assert response_json['error_code'] == 'bad_request'
            assert response_json['error_message'] == (
                'Invalid payload: {} error: '
                'Expecting value: line 1 column 1 (char 0)'
            )

    async def test_should_return_bad_request_when_partner_has_invalid_field(
        self,
        client,
        create_partner_url,
        create_partner_payload,
    ):

        del create_partner_payload['id']

        async with client.post(
            create_partner_url,
            json=create_partner_payload
        ) as response:
            assert response.status == 400

            response_json = await response.json()

            assert response_json['error_code'] == 'bad_request'
            assert response_json['error_message'] == (
                'Invalid partner payload: '
                '{\'id\': [\'Missing data for required field.\']}'
            )

    async def test_should_return_bad_request_when_empty_json(
        self,
        client,
        create_partner_url
    ):
        async with client.post(
            create_partner_url,
            json={}
        ) as response:
            assert response.status == 400
            response_json = await response.json()

            assert response_json['error_code'] == 'bad_request'
            assert response_json['error_message'] == 'Empty JSON payload: {}'

    async def test_should_conflict_when_partner_already_exists(
        self,
        client,
        create_partner_url,
        create_partner_payload,
        save_partner
    ):
        async with client.post(
            create_partner_url,
            json=create_partner_payload
        ) as response:
            assert response.status == 409

            response_json = await response.json()

            assert response_json['error_code'] == 'conflict'
            assert response_json['error_message'] == (
                'Partner with id:1 '
                'and document:1432132123891/0001 '
                'already exists'
            )
