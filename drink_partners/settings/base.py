import os
import sys

from drink_partners.settings import constants

SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    'CONFIGURE_LOGGING': True
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
            'require_debug_false': {
                '()': 'drink_partners.contrib.logs.filters.RequireDebugFalse'
            },
            'add_hostname': {
                '()': 'drink_partners.contrib.logs.filters.AddHostName'
            },
            'ignore_if_contains': {
                '()': 'drink_partners.contrib.logs.filters.IgnoreIfContains',
                'substrings': ['/healthcheck/']
            }
        },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(hostname)s %(name)s %(module)s:%(filename)s:%(lineno)d %(process)d %(thread)d == %(message)s'  # noqa
        },
        'simple': {
            'format': '%(hostname)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'stdout': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'simple',
            'filters': [
                'add_hostname',
                'ignore_if_contains'
            ],
        },
    },
    'loggers': {
        '': {
            'handlers': ['stdout'],
            'level': 'INFO',
            'propagate': True,
        },
        'asyncio': {
            'level': 'WARNING',
            'propagate': True,
        },
        'gunicorn.access': {
            'level': 'CRITICAL',
            'propagate': True,
        }
    }
}

# Auth applications
AUTH_APPLICATIONS = {
    'dev': os.getenv('APP_TOKEN', 'test')
}

POOL_OF_RAMOS = {
    'authentication': [
        constants.STATIC_AUTHORIZATION_BACKEND,
    ],
    'partners': [
        constants.MONGODB_PARTNERS_BACKEND,
    ],

}

MOTOR_DB = os.getenv('MOTOR_DB', 'drink_partners')
MOTOR_URI = os.environ.get('MONGODB_URI', f'mongodb://127.0.0.1:27017/{MOTOR_DB}') # noqa
MOTOR_MAX_POOL_SIZE = int(os.environ.get('MONGO_MAX_POOL_SIZE', '1'))
MOTOR_KWARGS = {}

DEFAULT_AUTH_BACKEND_ID = 'static'
DEFAULT_PARTNERS_BACKEND_ID = 'mongodb'
