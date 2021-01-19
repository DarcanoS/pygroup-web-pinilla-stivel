class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///shop.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATION = False
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True
    # SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR' \
    #              '"\xa1\xa8'
    SECRET_KEY = '19da83e8e3c7d5f28f6b12ccd3a613675eba07a8a46788dd316a2f7d31e1'
    # DATABASE_URI = 'sqlite://:memory:'


class TestingConfig(Config):
    TESTING = True