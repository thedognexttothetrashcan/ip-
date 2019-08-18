import hashlib

from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models.base import TeachBaseModel

"""
    设计权限
        0    啥权限都没
        1    读权限
        2    评论权限
        4    写帖子权限
        8    买票权限
"""

USER_READ = 1
USER_COMMENT = 2
USER_WRITE = 4
USER_BUY = 8


class User(TeachBaseModel):

    u_name = db.Column(db.String(16), unique=True)
    _u_password = db.Column(db.String(256))
    u_phone = db.Column(db.String(16), unique=True)
    is_delete = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)
    u_permission = db.Column(db.Integer, default=0)
    u_token = db.Column(db.String(64), default='')

    @property
    def u_password(self):
        # return self._u_password
        raise Exception("不许动")

    @u_password.setter
    def u_password(self, password):
        self._u_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._u_password, password)

    def check_permission(self, permission):
        return self.u_permission & permission == permission

    # def set_password(self, password):
    #     # self.u_password = hashlib.new("md5", password.encode("utf-8")).hexdigest()
    #     self.u_password = generate_password_hash(password)
    #
    # def verify_password(self, password):
    #     # return self.u_password == hashlib.new("md5", password.encode("utf-8")).hexdigest()
    #     return check_password_hash(self.u_password, password)
