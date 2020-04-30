from drink_partners.factory import build_app, get_middlewares


class TestFactory:

    def test_should_return_middlewares(self):
        assert get_middlewares() == []

    def test_should_build_app(self):
        assert build_app() is not None
