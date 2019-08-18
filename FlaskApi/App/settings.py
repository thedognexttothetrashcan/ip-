
def get_db_uri(dbinfo):

    db = dbinfo.get("db")
    driver = dbinfo.get("driver")
    user = dbinfo.get("user")
    password = dbinfo.get("password")
    host = dbinfo.get("host")
    port = dbinfo.get("port")
    name = dbinfo.get("name")

    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


class Config:

    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "rock1204"

    SESSION_TYPE = "redis"

    SESSION_USE_SIGNER = True


class DevelopConfig(Config):

    DEBUG = True

    DATABASE = {
        "db": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "rock1204",
        "host": "localhost",
        "port": "3306",
        "name": "BJ1806FlaskApi"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):

    TESTING = True


class ProductConfig(Config):
    pass


class StagingConfig(Config):
    pass


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}