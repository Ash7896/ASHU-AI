##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
