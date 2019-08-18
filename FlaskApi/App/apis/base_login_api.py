from flask import request, g
from flask_restful import Resource, abort

from App.models import User


class BaseResource(Resource):

    def check_login(self):
        u_token = request.args.get("u_token")

        users = User.query.filter(User.u_token == u_token).all()

        if not users:
            abort(401, message="用户身份失效")

        user = users[0]

        g.user = user

