import abc


class PartnersBackend(abc.ABC):

    @abc.abstractmethod
    async def get_by_id(self, id):  # pragma: no cover
        pass
