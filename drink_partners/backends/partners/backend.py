import abc


class PartnersBackend(abc.ABC):

    @abc.abstractmethod
    async def get_by_id(self, id):  # pragma: no cover
        pass

    @abc.abstractmethod
    async def get_by_document(self, document):  # pragma: no cover
        pass

    @abc.abstractmethod
    async def save(self, payload):  # pragma: no cover
        pass

    @abc.abstractmethod
    async def search_nearest_by_lng_lat(self, coordinate):  # pragma: no cover
        pass
