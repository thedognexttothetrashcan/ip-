from flask import request, g
from flask_restful import abort

from App.models import User


def login_required(fun):
    def wrap(*args, **kwargs):
        u_token = request.args.get("u_token")

        users = User.query.filter(User.u_token == u_token).all()

        if not users:
            abort(401, message="用户身份失效")

        user = users[0]

        g.user = user

        return fun(*args, **kwargs)

    return wrap


def require_permission(permission):
    def login_required(fun):
        def wrap(*args, **kwargs):
            u_token = request.args.get("u_token")

            users = User.query.filter(User.u_token == u_token).all()

            if not users:
                abort(401, message="用户身份失效")

            user = users[0]

            if not user.check_permission(permission):
                abort(403, message="你无权限操作此模块，请联系管理员")

            g.user = user

            return fun(*args, **kwargs)

        return wrap

    return login_required
