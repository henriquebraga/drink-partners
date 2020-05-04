import pytest

from drink_partners.contrib.samples import (
    partner_adega_cerveja,
    partner_adega_ze_ambev,
    partner_bar_legal
)


@pytest.fixture
def url():
    return '/partner/1/'


@pytest.fixture
def partner_with_str_id_url():
    return '/partner/id-str/'


@pytest.fixture
def partner_search_with_str_coordinates_url():
    return '/partner/search/lng/a/lat/a/'


@pytest.fixture
def partner_search_coordinates_url():
    return '/partner/search/lng/-43.36556/lat/-22.99669/'


@pytest.fixture
def partner_not_found_url():
    return '/partner/100/'


@pytest.fixture
def create_partner_url():
    return '/partner/'


@pytest.fixture
async def save_partner(mongo_database):
    partner_collection = mongo_database.get_collection('partners')
    await partner_collection.insert_one(partner_adega_cerveja())
    return partner_adega_cerveja()


@pytest.fixture
def create_partner_payload():
    return partner_adega_cerveja()


@pytest.fixture
async def save_partners(mongo_database):
    partners = [
        partner_adega_ze_ambev(),
        partner_bar_legal()
    ]

    for partner in partners:
        await mongo_database.get_collection('partners').insert_one(partner)

    return partners
