from drink_partners.settings import constants

# Auth applications
AUTH_APPLICATIONS = {
    'dev': 'test'
}

POOL_OF_RAMOS = {
    'authentication': [
        constants.STATIC_AUTHORIZATION_BACKEND,
    ]
}

DEFAULT_AUTH_BACKEND_ID = 'static'
