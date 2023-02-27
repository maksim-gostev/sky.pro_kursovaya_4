import json

from dao.model.genre import Genre
from dao.model.director import Director
from dao.model.movie import Movie
from config import Config
from app import create_app
from setup_db import db




if __name__ == '__main__':
    with create_app(Config).app_context():
        db.create_all()

        with open('fixtures.json', 'r', encoding='utf-8') as file:
            json_data:[list] = json.load(file)


        for json_genre in json_data['genres']:
            genre = Genre(
                id=json_genre['pk'],
                name=json_genre['name']
            )
            db.session.add(genre)

        for json_director in json_data['directors']:
            director = Director(
                id=json_director['pk'],
                name=json_director['name']
            )

            db.session.add(director)

        for json_movie in json_data['movies']:
            movie = Movie(
            title=json_movie['title'],
            description=json_movie['description'],
            trailer=json_movie['trailer'],
            year=json_movie['year'],
            rating=json_movie['rating'],
            genre_id=json_movie['genre_id'],
            director_id=json_movie['director_id'],
            id=json_movie['pk']
            )

            db.session.add(movie)

        db.session.commit()


