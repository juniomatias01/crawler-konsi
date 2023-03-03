class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'replace_with_a_secret_key'
    CRAWLER_BASE_URL = 'http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/'
    CRAWLER_ORIGIN = 'http://ionic-application.s3-website-sa-east-1.amazonaws.com'
    CRAWLER_REFERER = 'http://ionic-application.s3-website-sa-east-1.amazonaws.com'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
