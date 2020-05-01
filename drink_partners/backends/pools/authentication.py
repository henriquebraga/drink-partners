from ramos.mixins import DefaultBackendMixin
from ramos.pool import BackendPool


class AuthenticationBackendPool(DefaultBackendMixin, BackendPool):
    backend_type: str = 'authentication'
    SETTINGS_KEY: str = 'DEFAULT_AUTH_BACKEND_ID'
