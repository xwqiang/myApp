import os

from config import dev, prod, test


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'xu.wuqiang@kuyun.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://kuyun_oa:MSbiJU52w3e@192.168.200.22/kuyun_oa'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_POOL_RECYCLE = 60  # seconds
    SQLALCHEMY_MAX_OVERFLOW = 30
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    USERNAME = "aaabbb"
    SETTINGS = dev


class TestingConfig(Config):
    TESTING = True
    settings = test


class ProductionConfig(Config):
    settings = prod


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}
