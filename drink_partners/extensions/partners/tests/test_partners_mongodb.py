class TestPartnersMongoDbBackend:

    async def test_should_get_partner(self, backend, save_partner):
        partner = await backend.get_by_id('1')
        assert partner == save_partner
