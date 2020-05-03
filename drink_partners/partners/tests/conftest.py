import pytest

from drink_partners.contrib.samples import partner_adega_cerveja


@pytest.fixture
def url():
    return '/partner/1/'


@pytest.fixture
def partner_with_str_id_url():
    return '/partner/id-str/'


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
    return {
        'pdvs': [partner_adega_cerveja()]
    }
