class BaseConfig(object):
    """配置基类"""
    SECRETE_KEY = "Hiro_Huang"

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI="mysql://root:woaimiaomiao@localhost/simpledu?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    """生产环境配置"""
    pass

class TestingConfig(BaseConfig):
    """测试环境配置"""
    pass

configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
    }
