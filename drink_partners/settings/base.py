import os

from drink_partners.settings import constants

# Auth applications
AUTH_APPLICATIONS = {
    'dev': 'test'
}

POOL_OF_RAMOS = {
    'authentication': [
        constants.STATIC_AUTHORIZATION_BACKEND,
    ],
    'partners': [
        constants.MONGODB_PARTNERS_BACKEND,
    ],

}

MOTOR_DB = 'drink_partners'
MOTOR_URI = os.environ.get('MONGO_URI', f'mongodb://127.0.0.1:27017/{MOTOR_DB}') # noqa
MOTOR_MAX_POOL_SIZE = int(os.environ.get('MONGO_MAX_POOL_SIZE', '1'))
MOTOR_KWARGS = {}

DEFAULT_AUTH_BACKEND_ID = 'static'
DEFAULT_PARTNERS_BACKEND_ID = 'mongodb'
