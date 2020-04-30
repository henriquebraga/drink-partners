from drink_partners.factory import build_app, get_middlewares
from drink_partners.middlewares.exception_handler import (
    exception_handler_middleware
)


class TestFactory:

    def test_should_return_middlewares(self):
        assert get_middlewares() == [
            exception_handler_middleware
        ]

    def test_should_build_app(self):
        assert build_app() is not None
