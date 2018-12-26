import os


class Config:
    DEBUG = False
    CSRF_ENABLED = True


class Development(Config):
    DEBUG = True
    red_flags = {}


class Testing(Config):
    DEBUG = True
    TESTING = True


class Production(Config):
    DEBUG = False
    TESTING = False


class Staging(Config):
    DEBUG = True

app_config = {
    'DEVELOPMENT': Development, 'TESTING': Testing, 'PRODUCTION': Production,
    'STAGING': Staging
    }
