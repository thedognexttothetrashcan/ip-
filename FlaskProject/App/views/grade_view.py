from time import sleep

from flask import Blueprint, render_template

from App.ext import cache

blue_grade = Blueprint("blue_grade", __name__, url_prefix='/grade')


@blue_grade.route("/")
# @cache.cached(timeout=60)
def index():

    result = cache.get("index")

    if result:
        return result

    result = render_template("GradeList.html")

    sleep(5)

    cache.set("index", result, timeout=20)

    return result