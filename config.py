import conf
import psycopg2


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'postgresql://{conf.DB_USER}:{conf.DB_PASS}@localhost/{conf.DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
