
from dao.director_dao import DirectorDAO
from dao.favourite_movie_dao import FavouriteMovieDAO
from dao.genre_dao import GenreDAO
from dao.movie_dao import MovieDAO
from dao.user_dao import UserDAO
from service.auth_ser import AuthService
from service.director_ser import DirectorService
from service.favourite_movie_ser import FavouriteMovieService
from service.genre_ser import GenreService
from service.movie_ser import MovieService
from service.user_ser import UserService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)
f_movie_dao = FavouriteMovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)
f_movie_service = FavouriteMovieService(f_movie_dao)