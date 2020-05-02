import logging
import socket

from simple_settings import settings


class RequireDebugFalse(logging.Filter):
    def filter(self, record):
        return not settings.DEBUG


class AddHostName(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = self.hostname
        return True


class IgnoreIfContains(logging.Filter):
    def __init__(self, substrings=None):
        self.substrings = substrings or []

    def filter(self, record):
        message = record.getMessage()
        return not any(
            substrings in message
            for substrings in self.substrings
        )
