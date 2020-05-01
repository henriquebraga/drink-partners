import pytest


@pytest.fixture
def partner():
    return {
        'id': 1,
        'tradingName': 'Adega da Cerveja - Pinheiros',
        'ownerName': 'Zé da Silva',
        'document': '1432132123891/0001',
        'coverageArea': {
            'type': 'MultiPolygon',
            'coordinates': [
                [
                    [
                        [30, 20], [45, 40], [10, 40], [30, 20]
                    ]
                ],
                [
                    [
                        [15, 5], [40, 10], [10, 20], [5, 10], [15, 5]
                    ]
                ]
            ]
        },
        'address': {
            'type': 'Point',
            'coordinates': [-46.57421, -21.785741]
        },
    }


@pytest.fixture
async def save_partner(mongo_database, partner):
    partner_collection = mongo_database.get_collection('partners')
    await partner_collection.insert_one(partner)
    return partner
