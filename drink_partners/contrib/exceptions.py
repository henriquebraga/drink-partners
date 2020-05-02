class APIException(Exception):
    status_code = 500
    error_code = 'server_error'
    error_message = 'Internal server error.'
    error_details = None

    def __init__(
        self,
        error_code=None,
        error_message=None,
        error_details=None,
    ):
        if error_code:
            self.error_code = error_code

        if error_message:
            self.error_message = error_message

        if error_details:
            self.error_details = error_details

    def as_dict(self):
        data = {
            'error_code': self.error_code,
            'error_message': self.error_message,
        }
        if self.error_details:
            data['error_details'] = self.error_details

        return data


class NotFound(APIException):
    status_code = 404
    error_code = 'not_found'
    error_message = 'Not Found'


class BadRequest(APIException):
    status_code = 400
    error_code = 'bad_request'
    error_message = 'Bad Request'


class PartnerAlreadyExists(Exception):

    def __init__(self, partner_id, document):
        self.partner_id = partner_id
        self.document = document

    def __str__(self):
        return (
            f'Partner with id:{self.partner_id}'
            f'and document:{self.document} already exists'
        )
