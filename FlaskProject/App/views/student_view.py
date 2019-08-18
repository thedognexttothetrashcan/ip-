from flask import Blueprint

blue_student = Blueprint("blue_student", __name__, url_prefix='/student')


@blue_student.route("/")
def index():
    return "student index"