from App.apis.base_login_api import BaseResource


class CommentResource(BaseResource):

    def post(self):

        self.check_login()

        return {"msg": "评论成功"}