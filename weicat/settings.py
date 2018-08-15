class Config(object):
    AppID = ''
    AppSecret=''


# 上线
class ProductionConfig(Config):
    DEBUG = False
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# 开发模式
class DevelopmentConfig(Config):
    DEBUG = True
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# 测试
class TestingConfig(Config):
    TESTING = True
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
