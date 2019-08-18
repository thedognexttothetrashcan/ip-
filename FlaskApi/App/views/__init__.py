from App.views.aop import aop_blue
from App.views.session_view import blue


def init_blue(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=aop_blue)
