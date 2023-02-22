from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
from service.decorators import auth_required

movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        page = request.args.get("page")
        status = request.args.get("status")
        filters = {
            "page": page,
            "status": status
        }
        all_movies = movie_service.get_all(filters)

        return movies_schema.dump(all_movies), 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        if not movie:
            return "такого фильма нет", 404
        return movie_schema.dump(movie), 200
