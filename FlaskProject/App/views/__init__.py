from App.views.grade_view import blue_grade
from App.views.movie_view import movie_blue
from App.views.student_view import blue_student


def init_blue(app):
    app.register_blueprint(blueprint=blue_student)
    app.register_blueprint(blueprint=blue_grade)
    app.register_blueprint(blueprint=movie_blue)

