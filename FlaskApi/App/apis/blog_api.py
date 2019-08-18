from flask import request, g
from flask_restful import Resource

from App.apis.user_dectorator import login_required
from App.models import User


class BlogsResource(Resource):

    # def post(self):
    #
    #     u_token = request.args.get("u_token")
    #
    #     users = User.query.filter(User.u_token == u_token).all()
    #
    #     if not users:
    #
    #         data = {
    #             "status": 605,
    #             "msg": "not login"
    #         }
    #
    #         return data
    #
    #     user = users[0]
    #
    #     pass
    #     # 发表帖子一套逻辑
    #     # 帖子和用户进行绑定
    #
    #     data = {
    #         "status": 200,
    #         "msg": "ok"
    #     }
    #
    #     return data

    @login_required
    def post(self):

        user = g.user

        return {"msg": "哈哈%s" % user.u_name}
