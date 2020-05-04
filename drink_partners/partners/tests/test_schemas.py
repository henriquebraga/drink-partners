import pytest

from drink_partners.contrib.samples import partner_adega_cerveja
from drink_partners.partners.schemas import PartnerSchema


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

    def test_schema_should_return_error_when_address_has_invalid_type(self):
        partner = partner_adega_cerveja()

        partner['address']['type'] = 'invalid-type'

        schema = PartnerSchema()
        errors = schema.validate(partner)
        assert errors == {'address': {'type': ['Type must be Point']}}

    def test_schema_should_return_error_when_address_has_invalid_point(self):
        partner = partner_adega_cerveja()

        partner['address']['coordinates'] = [0, 1, 2]

        schema = PartnerSchema()
        errors = schema.validate(partner)

        assert errors == {
            'address': {
                'coordinates': [
                    'Points must have exactly two coordinates: [lng, lat]'
                ]
            }
        }

    def test_schema_should_return_error_coverage_area_has_invalid_multipolygon(self): # noqa
        partner = partner_adega_cerveja()

        partner['coverageArea']['coordinates'] = [[0, 1]]

        schema = PartnerSchema()
        errors = schema.validate(partner)

        assert errors == {
            'coverageArea': {
                'coordinates': {
                    0: {
                        0: ['Not a valid list.'],
                        1: ['Not a valid list.']
                    }
                }
            }
        }

    def test_schema_should_return_error_when_address_has_id_as_str(self):
        partner = partner_adega_cerveja()
        partner['id'] = '1'
        schema = PartnerSchema()
        errors = schema.validate(partner)

        assert errors == {}
