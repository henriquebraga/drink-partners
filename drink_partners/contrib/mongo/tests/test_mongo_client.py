import pytest

from drink_partners.contrib.mongo.client import MongoClient


class TestMongoClient:

    @pytest.fixture()
    def mongo1(self):
        return MongoClient()

    @pytest.fixture()
    def mongo2(self):
        return MongoClient()

    def test_should_be_same_instance(self, mongo1, mongo2):
        assert mongo1 is mongo2

    def test_should_return_drink_partners_database(self, mongo1):
        assert mongo1.db.name == 'drink_partners_test'

    def test_should_return_collection_name(self, mongo1):
        assert mongo1.get_collection('partners').name == 'partners'

    def test_should_client_as_none(self, mongo1):
        mongo1.close()
        assert mongo1._client is None
