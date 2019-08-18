from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.middleware import load_middleware
from App.settings import envs
from App.views import init_blue


def create_app(env):

    app = Flask(__name__)

    # 初始化App
    app.config.from_object(envs.get(env))

    # 初始化扩展库
    init_ext(app=app)

    # 初始化路由
    init_api(app=app)
    init_blue(app=app)
    # 加载中间件
    load_middleware(app=app)

    return app