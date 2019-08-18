import time

from flask import request
from flask_restful import abort

from App.ext import cache

PATH_LIST = ["/goods/"]

PERMISSION_BUY_LIST = []


def load_middleware(app):
    @app.before_request
    def before():

        # path = request.path
        #
        # if path in PATH_LIST:
        #     u_token = request.args.get("u_token")
        #
        #     users = User.query.filter(User.u_token == u_token).all()
        #
        #     if not users:
        #         abort(401, message="用户身份失效")
        #
        #     user = users[0]
        #
        #     g.user = user

        # path = request.path
        #
        # if path == "/getphone/":
        #     if request.method == "POST":
        #         # username = request.form.get("username")
        #         #
        #         # if username.startswith("Rock"):
        #         #     return "恭喜你免费获得小米8探索版"
        #
        #         ip = request.remote_addr
        #
        #         if ip.startswith("10.0.118.1"):
        #             if random.randrange(100) > 30:
        #                 return "恭喜你成功抢到小米8探索版"
        #
        # elif path == "/search/":
        #
        #     if request.method == "POST":
        #
        #         ip = request.remote_addr
        #
        #         result = cache.get(ip)
        #
        #         if result:
        #             return "您的查询频率有点频繁，十秒之内搜索一次"
        #
        #         cache.set(ip, "哈哈哈", timeout=10)

        path = request.path

        if not path.startswith("/_debug"):

            ip = request.remote_addr

            black_list = cache.get("black") or []

            if ip in black_list:
                # abort(400, message="小伙子，爬虫获取十条数据就是三年")
                return "小伙子，爬虫获取十条数据就是三年", 400

            request_list = cache.get(ip)

            if request_list:

                """
                    [11:42:05, 11:42:07, 11:43:10, 11:43:33]
                    
                    反转时间
                    [11:47:50, 11:47:30, 11:47:22, 11:46:55...]
                """
                while request_list and time.time() - request_list[-1] >= 60:
                    request_list.pop()

                if len(request_list) > 60:
                    black_list.append(ip)
                    cache.set("black", black_list, timeout=60*60*24)
                    # abort(400, message="小爬虫回家睡觉吧")
                    return "小爬虫回家睡觉吧", 400

                if len(request_list) > 30:
                    request_list.insert(0, time.time())
                    cache.set(ip, request_list, timeout=60)
                    return "您的请求频率过高"
            else:
                request_list = []

            print(ip, len(request_list))
            request_list.insert(0, time.time())
            cache.set(ip, request_list, timeout=60)
