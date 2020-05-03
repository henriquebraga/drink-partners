import pytest
from geojson import Point

from drink_partners.contrib.exceptions import PartnerAlreadyExists
from drink_partners.contrib.samples import (
    partner_adega_cerveja,
    partner_adega_ze_ambev,
    partner_bar_legal
)


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

    async def test_should_search_partner_by_coordinate(
        self,
        backend
    ):
        partner = partner_adega_ze_ambev()
        coordinate = partner['coverageArea']['coordinates'][0][0][0]

        await backend.save(partner)

        point = Point(coordinate)

        found_partner = await backend.search_nearest_by_coordinate(
            coordinate=point
        )

        assert found_partner == partner_adega_ze_ambev()

    async def test_should_search_by_coordinate_nearest_address_partner(
        self,
        backend
    ):
        partner = partner_adega_ze_ambev()
        nearest_partner = partner_bar_legal()

        coordinate = partner['coverageArea']['coordinates'][0][0][0]

        await backend.save(partner)
        await backend.save(nearest_partner)

        point = Point(coordinate)

        found_partner = await backend.search_nearest_by_coordinate(
            coordinate=point
        )

        assert found_partner == nearest_partner

    async def test_search_partner_by_coordinate_be_none_when_no_partner_found(
        self,
        backend
    ):
        partner = partner_adega_ze_ambev()
        coordinate = [0, 0]

        await backend.save(partner)

        point = Point(coordinate)

        found_partner = await backend.search_nearest_by_coordinate(
            coordinate=point
        )

        assert found_partner is None
