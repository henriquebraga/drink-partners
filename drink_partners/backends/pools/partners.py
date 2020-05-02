from ramos.mixins import DefaultBackendMixin  # pragma: no cover
from ramos.pool import BackendPool  # pragma: no cover


class PartnersBackendPool(DefaultBackendMixin, BackendPool):  # pragma: no cover # noqa
    backend_type: str = 'partners'
    SETTINGS_KEY: str = 'DEFAULT_PARTNERS_BACKEND_ID'
