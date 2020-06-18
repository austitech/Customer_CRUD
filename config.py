
class Config:
    SECRET_KEY = None


class DevelopmentConfig(Config):
    SECRET_KEY = "jjhjpfiiofjishrshrsuhrhszurhgurils"
    DEBUG = True


class ProductionConfig(Config):
    pass
