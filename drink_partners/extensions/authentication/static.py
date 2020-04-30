from ramos.mixins import SingletonCreateMixin
from simple_settings import settings

from drink_partners.backends.authentication.backend import (
    AuthenticationBackend
)


class StaticAuthenticationBackend(SingletonCreateMixin, AuthenticationBackend):
    id = 'static'
    name = 'Static Authentication'

    AUTH_HEADER = 'Authorization'

    async def authenticate(self, request):
        token = self._get_token(request)

        if not token:
            return

        for name, application_token in settings.AUTH_APPLICATIONS.items():
            if application_token == token:
                return {'name': name, 'active': True}

    def _get_token(self, request):
        if 'token' in request.url.query:
            return request.url.query['token']
        elif self.AUTH_HEADER in request.headers:
            return request.headers[self.AUTH_HEADER]
