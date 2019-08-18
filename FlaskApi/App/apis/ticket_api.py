from flask import g
from flask_restful import Resource, abort

from App.apis.user_dectorator import login_required, require_permission
from App.models.user_model import USER_BUY, USER_READ


class TicketResource(Resource):

    # @login_required
    # def post(self):
    #
    #     user = g.user
    #
    #     if user.check_permission(USER_BUY):
    #
    #         return {"msg": "票票票%s" % user.u_name}
    #     else:
    #
    #         abort(403, message="你没有权限访问此模块，如有疑问请联系管理员")

    @require_permission(USER_READ)
    def post(self):

        return {"msg": "哈哈，包场了"}