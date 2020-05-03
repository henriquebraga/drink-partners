import pytest

from drink_partners.contrib.exceptions import PartnerAlreadyExists
from drink_partners.contrib.samples import partner_adega_cerveja


class TestPartnersMongoDbBackend:

    async def test_should_get_partner(self, backend, save_partner):
        partner = await backend.get_by_id('1')
        assert partner == save_partner

    async def test_should_get_by_document(self, backend, save_partner):
        partner = await backend.get_by_document('1432132123891/0001')

        assert partner == save_partner

    async def test_should_raise_exception_when_saving_existing_partner(
        self,
        backend,
        save_partner
    ):

        with pytest.raises(PartnerAlreadyExists) as error:
            await backend.save(save_partner)

        assert str(error.value) == (
            'Partner with id:1 and document:1432132123891/0001 already exists'
        )

    async def test_should_save_partner(
        self,
        backend,
        mongo_database
    ):
        await backend.save(partner_adega_cerveja())
        partner = await backend.get_by_document(
            partner_adega_cerveja()['document']
        )

        assert partner == partner_adega_cerveja()
