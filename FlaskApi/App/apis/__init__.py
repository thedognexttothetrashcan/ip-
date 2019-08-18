from flask_restful import Api

from App.apis.blog_api import BlogsResource
from App.apis.comment_api import CommentResource
from App.apis.goods_api import GoodsResource
from App.apis.movie_api import MoviesResource, MovieResource
from App.apis.ticket_api import TicketResource
from App.apis.user_api import UsersResource, UserResource

api = Api()


def init_api(app):
    api.init_app(app=app)


api.add_resource(MoviesResource, "/movies/")
api.add_resource(MovieResource, "/movies/<int:id>/")

api.add_resource(UsersResource, "/users/")

api.add_resource(UserResource, "/user/")

api.add_resource(BlogsResource, "/blogs/")

api.add_resource(TicketResource, "/tickets/")

api.add_resource(CommentResource, "/comments/")

api.add_resource(GoodsResource, "/goods/")