from marshmallow import Schema, ValidationError, fields, pre_load, validate


def validate_point(points):
    if len(points) != 2:
        raise ValidationError(
            'Points must have exactly two coordinates: [lng, lat]'
        )


class CoverageAreaSchema(Schema):
    type = fields.Str(
        required=True,
        validate=[
            validate.OneOf(
                [
                    'MultiPolygon',
                ],
                error='Type must be {choices}'
            )
        ]
    )

    coordinates = fields.List(
        fields.List(
            fields.List(
                fields.List(
                    fields.Float(), validate=[validate_point]
                )
            )
        )
    )


class AddressSchema(Schema):

    type = fields.Str(
        required=True,
        validate=[
            validate.OneOf(
                [
                    'Point',
                ],
                error='Type must be {choices}'
            )
        ]
    )
    coordinates = fields.List(fields.Float(), validate=[validate_point])


class PartnerSchema(Schema):

    id = fields.Int(required=True)

    tradingName = fields.Str(required=True)
    ownerName = fields.Str(required=True)
    document = fields.Str(required=True)
    coverageArea = fields.Nested(CoverageAreaSchema(), required=True)
    address = fields.Nested(AddressSchema(), required=True)

    @pre_load
    def parse_id_to_int(self, in_data, **kwargs):
        _id = in_data.get('id')
        if _id:
            in_data['id'] = int(_id)
        return in_data
