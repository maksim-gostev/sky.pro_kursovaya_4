
from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors_views import director_ns
from views.genres_views import genre_ns
from views.movies_views import movie_ns
from views.user_views import user_ns
from views.auth_view import auth_ns
from views.favourite_movie import f_movie_ns


def create_app(config_object: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """Инициализация базы данных и неймспейсов"""
    db.init_app(app)
    api = Api(app)
    # добовление "НС"
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(f_movie_ns)


app = create_app(Config())
app.debug = True



if __name__ == '__main__':
    app.run()

