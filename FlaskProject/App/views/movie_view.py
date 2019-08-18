from flask import Blueprint, request, jsonify
from App.models import Movie

movie_blue = Blueprint("movie_blue", __name__, url_prefix="/api")


@movie_blue.route("/movies/", methods=["GET", "POST"])
@movie_blue.route("/movies/<int:id>/", methods=["GET", "POST", "DELETE"])
def movies(id=0):
    if request.method == "GET":

        if id == 0:

            movie_list = Movie.query.all()

            movie_list_tran = []

            for movie in movie_list:
                movie_list_tran.append(movie.to_dict())

            data = {
                "status": 200,
                "msg": "ok",
                "data": movie_list_tran
            }

            return jsonify(data)
        else:

            movie = Movie.query.get(id)

            data = {
                "status": 200,
                "msg": "ok",
                "data": movie.to_dict()
            }

            return jsonify(data)

    elif request.method == "POST":

        data = {
            "status": 201,
        }

        if id == 0:

            m_name = request.form.get("m_name")
            m_duration = request.form.get("m_duration")

            # 写代码验证
            movie = Movie()
            movie.m_name = m_name
            movie.m_duration = m_duration

            movie.save()
            data["msg"] = "create success"

        else:

            m_name = request.form.get("m_name")
            m_duration = request.form.get("m_duration")

            movie = Movie.query.get(id)

            movie.m_name = m_name
            movie.m_duration = m_duration

            movie.save()
            data["msg"] = "modify success"

        data["data"] = movie.to_dict()
        return jsonify(data)
    elif request.method == "DELETE":
        if id:
            movie = Movie.query.get(id)

            if movie:

                if movie.delete():

                    data = {
                        "status": 204,
                        "msg": "delete success"
                    }

                    return jsonify(data)
                else:

                    data = {
                        "msg": "fail",
                        "status": 602
                    }

                    return jsonify(data)
            else:
                data = {
                    "msg": "fail",
                    "status": 601
                }

                return jsonify(data)
