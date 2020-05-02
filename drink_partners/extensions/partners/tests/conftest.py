import pytest
from drink_partners.extensions.partners.mongodb import PartnersMongoDbBackend
from drink_partners.contrib.samples import partner_adega_cerveja


@pytest.fixture
def backend():
    return PartnersMongoDbBackend.create()


@pytest.fixture
async def save_partner(mongo_database):
    partner_collection = mongo_database.get_collection('partners')
    await partner_collection.insert_one(partner_adega_cerveja())
    return partner_adega_cerveja()
