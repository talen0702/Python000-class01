class Config(object):
    MYSQL_HOST = '10.100.3.12'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWD = 'rootroot'
    MYSQL_DB = 'test'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8&connect_timeout=10'
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True