class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = $secret.password #Can be any password
    MYSQL_DATABASE_HOST = '127.0.0.1:3306'
    MYSQL_DATABASE_DB = 'charity'  # can be any

    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    MYSQL_DATABASE_USER = 'yourusername'
    MYSQL_DATABASE_PASSWORD = 'yourpassword'
    MYSQL_DATABASE_HOST = 'linktoyourdb' # eg to amazone db :- yourdbname.xxxxxxxxxx.us-east-2.rds.amazonaws.com
    MYSQL_DATABASE_DB = 'yourdbname'

    DEBUG = False
