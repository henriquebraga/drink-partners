from drink_partners.contrib.logs.streams import LogDiscarder

from .base import *  # noqa; noqa

MOTOR_DB = 'drink_partners_test'

DEBUG = True

LOGGING['handlers']['stdout'] = {  # type: ignore # noqa
    'level': 'DEBUG',
    'class': 'logging.StreamHandler',
    'stream': LogDiscarder,
    'filters': []
}

for logger_name in LOGGING['loggers'].keys():  # type: ignore # noqa
    LOGGING['loggers'][logger_name]['handlers'] = ['stdout']  # type: ignore # noqa
