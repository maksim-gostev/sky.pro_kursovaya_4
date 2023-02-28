from flask_restx import Resource, Namespace


from dao.model.genre import GenreSchema
from implemented import genre_service


genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route('')
class  GenresView(Resource):

    def get(self):
        genre = genre_service.get_all()
        return genres_schema.dump(genre)



@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        genre = genre_service.get_dy_id(gid)
        if not genre:
            return "такого жанра нет", 404
        return genre_schema.dump(genre), 201
