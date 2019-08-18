from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 60
})
session_redis = Session()
toolbar = DebugToolbarExtension()


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    cache.init_app(app=app)
    session_redis.init_app(app=app)
    toolbar.init_app(app=app)