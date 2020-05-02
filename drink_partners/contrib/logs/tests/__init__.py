import socket
from unittest.mock import Mock

import pytest
from simple_settings.utils import settings_stub

from drink_partners.contrib.logs.filters import (
    AddHostName,
    IgnoreIfContains,
    RequireDebugFalse
)


class TestRequireDebugFalseFilter:

    @pytest.fixture
    def log_filter(self):
        return RequireDebugFalse()

    @pytest.mark.parametrize('debug,expected', (
        (True, False),
        (False, True)
    ))
    def test_should_return_check_value_of_debug_setting(
        self,
        debug,
        expected,
        log_filter
    ):
        with settings_stub(DEBUG=debug):
            assert log_filter.filter(None) is expected


class TestAddHostName:

    @pytest.fixture
    def log_filter(self):
        return AddHostName()

    @pytest.fixture
    def hostname(self):
        return socket.gethostname()

    def test_should_always_return_true(self, log_filter):
        assert log_filter.filter(Mock()) is True

    def test_should_add_attribute_hostname_to_log_record(self, log_filter):
        class Dummy:
            pass

        record = Dummy()
        log_filter.filter(record)

        assert hasattr(record, 'hostname')

    def test_should_add_hostname_to_log_record(self, log_filter, hostname):
        record = Mock()
        log_filter.filter(record)

        assert record.hostname == hostname


class TestIgnoreIfContains:

    @pytest.fixture
    def log_filter(self):
        return IgnoreIfContains(['/healthcheck/'])

    @pytest.mark.parametrize('message,expected', (
        ('GET /healthcheck/', False),
    ))
    def test_should_ignore_healthcheck_log_messages(
        self,
        message,
        expected,
        log_filter
    ):
        record = Mock(getMessage=lambda: message)
        assert log_filter.filter(record) is expected
