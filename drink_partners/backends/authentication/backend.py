import abc

from requests.models import Response


class AuthenticationBackend(abc.ABC):

    @abc.abstractmethod
    def authenticate(self, request: Response):  # pragma: no cover
        pass
