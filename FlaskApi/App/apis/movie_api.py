from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from App.models import Movie

parse = reqparse.RequestParser()

parse.add_argument("m_name", type=str, required=True, help = "请输入电影名字")
parse.add_argument("m_duration", type=int)

movies_fields = {
    "id": fields.Integer,
    "name": fields.String(attribute="m_name"),
    "m_duration": fields.Integer
}

movies_single_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(movies_fields)
}

movies_list_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(movies_fields))
}


class MoviesResource(Resource):
    # @marshal_with(movies_get_fields)
    def get(self):

        movies = Movie.query.all()

        data = {
            "status": 200,
            "msg": "ok",
            "data": movies
        }

        return marshal(data, movies_list_fields)

    @marshal_with(movies_single_fields)
    def post(self):

        args = parse.parse_args()

        m_name = args.get("m_name")
        m_duration = args.get("m_duration")

        movie = Movie()

        movie.m_name = m_name
        movie.m_duration = m_duration

        movie.save()

        data = {
            "status": 201,
            "msg": "create ok",
            "data": movie
        }

        return data


class MovieResource(Resource):

    @marshal_with(movies_single_fields)
    def get(self, id):

        movie = Movie.query.get(id)

        data = {
            "status": 200,
            "msg": "ok",
            "data": movie
        }

        return data

    @marshal_with(movies_single_fields)
    def post(self, id):

        movie = Movie.query.get(id)

        args = parse.parse_args()

        m_name = args.get("m_name")

        m_duration = args.get("m_duration")

        movie.m_name = m_name

        movie.m_duration = m_duration

        movie.save()

        data = {
            "status": 201,
            "msg": "modify success",
            "data": movie
        }

        return data
    
    def delete(self,id):

        movie = Movie.query.get(id)

        movie.delete()

        data = {
            "status": 204,
            "msg": "delete success",
        }

        return data