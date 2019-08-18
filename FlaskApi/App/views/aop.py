import random

from flask import Blueprint, request, render_template

aop_blue = Blueprint("aop_blue", __name__)


@aop_blue.route("/getphone/", methods=["GET", "POST"])
def get_phone():
    if request.method == "GET":
        return render_template("get_phone.html")
    elif request.method == "POST":

        username = request.form.get("username")

        if random.randrange(100) >90:
            return "恭喜%s抢到小米8探索版" % username
        return "正在排队"


@aop_blue.route("/search/", methods=["GET", "POST"])
def search():

    if request.method == "GET":
        return render_template("search.html")
    elif request.method == "POST":

        keywords = request.form.get("keywords")

        return "查询出关于%s 100条信息" % keywords

