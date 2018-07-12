class Config(object):
    pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://blog:blog@localhost/blog_dev'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://blog:blog@localhost/blog'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}