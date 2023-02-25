from flask import request
from flask_restx import Namespace, Resource

from implemented import f_movie_service, user_service
from service.decorators import auth_required

f_movie_ns = Namespace("favorites/movies")

@f_movie_ns.route('/<int:mid>')
class FavaritMovieView(Resource):
    def post(self, mid):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404
        req_json['movie_id'] = mid

        f_movie_service.create(req_json)

        return "Фильм добавлен", 201


    @auth_required
    def delete(self, mid):
        auth_data = request.headers['Authorization']
        user = user_service.get_user_by_token(auth_data)
        f_movie_service.delete(mid, user.id)
        return "", 204