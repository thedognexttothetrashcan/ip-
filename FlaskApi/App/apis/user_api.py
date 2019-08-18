import uuid

from flask import request
from flask_restful import Resource, reqparse, fields, marshal

from App.models import User
from App.status_code import NOT_EXIST

parse = reqparse.RequestParser()

parse.add_argument("u_name", type=str, required=True, help="请提供用户名")
parse.add_argument("u_password", type=str, required=True, help="请提供密码")
parse.add_argument("u_phone", type=str, required=True, help="请提供手机号")
parse.add_argument("action", type=str, required=True, help="请正确输如参数")

user_fields = {
    "u_name": fields.String,
    "u_phone": fields.String,
    "is_active": fields.Boolean,
    "u_token": fields.String,
}

users_single_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(user_fields)
}

ACTION_LOGIN = "login"
ACTION_REGISTER = "register"


class UsersResource(Resource):

    def post(self):

        args = parse.parse_args()

        action = args.get("action")

        u_name = args.get("u_name")
        u_password = args.get("u_password")
        u_phone = args.get("u_phone")

        if action == ACTION_LOGIN:
            # users = User.query.filter(User.u_name.__eq__(u_name)).all()
            #
            # if len(users):
            #     user = users[0]
            #
            #     if user.verify_password(u_password):
            #         data = {
            #            "status": 200,
            #             "msg": "ok",
            #             "data": user
            #         }
            #         return marshal(data, users_single_fields)
            #     else:
            #
            #         data = {
            #             "status": 603,
            #             "msg": "密码错误"
            #         }
            #
            #         return data
            #
            # else:
            #     data = {
            #         "status": 604,
            #         "msg": "user does not exist"
            #     }
            #
            #     return data

            users = User.query.filter(User.u_name.__eq__(u_name)).all()

            if not len(users):
                data = {
                    "status": 604,
                    "msg": "user does not exist"
                }

                return data

            user = users[0]

            if not user.verify_password(u_password):
                data = {
                    "status": 603,
                    "msg": "密码错误"
                }

                return data
            u_token = str(uuid.uuid4())
            user.u_token = u_token
            user.save()

            data = {
                "status": 200,
                "msg": "ok",
                "data": user
            }
            return marshal(data, users_single_fields)

        elif action == ACTION_REGISTER:

            user = User()

            user.u_name = u_name

            # md5 = hashlib.new("md5", u_password.encode("utf-8"))
            # u_password = md5.hexdigest()

            # md5 = hashlib.md5()
            # md5.update(u_password.encode("utf-8"))
            # u_password = md5.hexdigest()

            user.u_password = u_password
            # user.set_password(u_password)

            user.u_phone = u_phone

            user.save()

            data = {
                "status": 201,
                "msg": "create success",
                "data": user
            }

            return marshal(data, users_single_fields)


class UserResource(Resource):

    def get(self):
        u_token  = request.args.get("u_token")

        users = User.query.filter(User.u_token == u_token).all()

        if not users:
            data = {
                "status": NOT_EXIST,
                "msg": "用户身份失效"
            }
            return data

        user = users[0]

        data = {
            "status": 200,
            "msg": "ok",
            "data": user
        }

        return marshal(data, users_single_fields)
