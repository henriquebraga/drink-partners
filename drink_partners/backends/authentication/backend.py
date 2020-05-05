import abc


class AuthenticationBackend(abc.ABC):

    @abc.abstractmethod
    def authenticate(self, request):  # pragma: no cover
        pass
