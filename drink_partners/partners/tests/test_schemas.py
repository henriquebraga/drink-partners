import pytest

from drink_partners.contrib.samples import partner_adega_cerveja
from drink_partners.partners.schemas import (
    AddressSchema,
    CoverageAreaSchema,
    PartnerSchema
)


class TestCoverageAreaSchema:

    def test_schema_should_validate_with_no_errors(self):
        coverage_area = partner_adega_cerveja()['coverageArea']
        schema = CoverageAreaSchema()
        errors = schema.validate(coverage_area)
        assert errors == {}

    @pytest.mark.parametrize('field', (
        'type',
        'coordinates',
    ))
    def test_schema_should_return_errors_when_missing_field(self, field):
        coverage_area = partner_adega_cerveja()['coverageArea']
        del coverage_area[field]

        schema = CoverageAreaSchema()
        errors = schema.validate(coverage_area)

        assert errors == {field: ['Missing data for required field.']}

    def test_schema_should_return_error_coordinates_has_invalid_multipolygon(self): # noqa
        coverage_area = partner_adega_cerveja()['coverageArea']
        coverage_area['coordinates'] = [[0, 1]]

        schema = CoverageAreaSchema()
        errors = schema.validate(coverage_area)

        assert errors == {
            'coordinates': {
                0: {
                    0: ['Not a valid list.'],
                    1: ['Not a valid list.']
                }
            }
        }

    def test_schema_should_return_error_when_coverage_area_has_invalid_type(self): # noqa
        coverage_area = partner_adega_cerveja()['coverageArea']
        coverage_area['type'] = 'invalid-type'

        schema = CoverageAreaSchema()
        errors = schema.validate(coverage_area)

        assert errors == {'type': ['Type must be MultiPolygon']}


class TestAddressSchema:

    def test_schema_should_validate_with_no_errors(self):
        address = partner_adega_cerveja()['address']
        schema = AddressSchema()
        errors = schema.validate(address)

        assert errors == {}

    @pytest.mark.parametrize('field', (
        'type',
        'coordinates',
    ))
    def test_schema_should_return_errors_when_missing_field(self, field):
        address = partner_adega_cerveja()['address']
        del address[field]

        schema = AddressSchema()
        errors = schema.validate(address)

        assert errors == {field: ['Missing data for required field.']}

    def test_schema_should_return_error_when_invalid_type(self):
        address = partner_adega_cerveja()['address']
        address['type'] = 'invalid-type'

        schema = AddressSchema()
        errors = schema.validate(address)

        assert errors == {'type': ['Type must be Point']}

    def test_schema_should_return_error_when_invalid_coordinates_format(self):
        address = partner_adega_cerveja()['address']
        address['coordinates'] = [0, 0, 0]

        schema = AddressSchema()
        errors = schema.validate(address)

        assert errors == {
            'coordinates': [
                'Points must have exactly two coordinates: [lng, lat]'
            ]
        }


class TestPartnerSchema:

    def test_schema_should_validate_with_no_errors(
        self
    ):
        schema = PartnerSchema()
        errors = schema.validate(partner_adega_cerveja())
        assert errors == {}

    @pytest.mark.parametrize('field', (
        'id',
        'tradingName',
        'document',
        'coverageArea',
        'address',
    ))
    def test_schema_should_return_errors_when_missing_field(
        self,
        field
    ):
        partner = partner_adega_cerveja()
        del partner[field]

        schema = PartnerSchema()
        errors = schema.validate(partner)

        assert errors == {field: ['Missing data for required field.']}

    def test_schema_should_return_error_when_address_has_id_as_str(self):
        partner = partner_adega_cerveja()
        partner['id'] = '1'
        schema = PartnerSchema()
        errors = schema.validate(partner)

        assert errors == {}
