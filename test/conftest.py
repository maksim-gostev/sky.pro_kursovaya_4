import pytest
from unittest.mock import MagicMock

from dao.director_dao import DirectorDAO
from dao.favourite_movie_dao import FavouriteMovieDAO
from dao.genre_dao import GenreDAO
from dao.movie_dao import MovieDAO
from dao.user_dao import UserDAO
from dao.model.favorite_movie import FavouriteMovie
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.model.user import User


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    test_director1 = Director(id=1, name="director1")
    test_director2 = Director(id=2, name="director2")
    test_director3 = Director(id=3, name="director3")

    test_directors = {1: test_director1, 2: test_director2, 3: test_director3}

    director_dao.get_all = MagicMock(return_value=test_directors.values())
    director_dao.get_by_id = MagicMock(return_value=test_director1)

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    test_genre1 = Genre(id=1, name="genre1")
    test_genre2 = Genre(id=2, name="genre2")
    test_genre3 = Genre(id=3, name="genre3")

    test_genres = {1: test_genre1, 2: test_genre2, 3: test_genre3}

    genre_dao.get_all = MagicMock(return_value=test_genres.values())
    genre_dao.get_by_id = MagicMock(return_value=test_genre1)

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    test_movie1 = Movie(
        id=1,
        title='title1',
        description='description1',
        trailer='trailer1',
        year=2001,
        rating=1.0,
        genre_id=1,
        genre='genre1',
        director_id=1,
        director='director1'
    )

    test_movie2 = Movie(
        id=2,
        title='title2',
        description='description2',
        trailer='trailer2',
        year=2002,
        rating=2.0,
        genre_id=2,
        genre='genre2',
        director_id=2,
        director='director2'
    )

    test_movie3 = Movie(
        id=3,
        title='title3',
        description='description3',
        trailer='trailer3',
        year=2003,
        rating=3.0,
        genre_id=3,
        genre='genre3',
        director_id=3,
        director='director3',
    )

    test_movies = {1: test_movie1, 2: test_movie2, 3: test_movie3}

    movie_dao.get_all = MagicMock(return_value=test_movies.values())
    movie_dao.get_by_id = MagicMock(return_value=test_movie1)
    movie_dao.get_by_new = MagicMock(return_value=test_movies.values())
    movie_dao.get_all_paginate = MagicMock(return_value=test_movies.values())
    movie_dao.get_by_year_paginate = MagicMock(return_value=test_movies.values())

    return movie_dao


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    test_user1 = User(
        id=1,
        email='email1',
        password='password1',
        name='name1',
        surname='surname1',
        favorite_genre=1
    )

    user_dao.get_one = MagicMock(return_value=test_user1)
    user_dao.get_by_email = MagicMock(return_value=test_user1)
    user_dao.create = MagicMock(return_value=User(
            id=4,
            email='email4',
            password='password4',
            name='name4',
            surname='surname4',
            favorite_genre=4
        ))

    return user_dao


@pytest.fixture()
def favourite_movie_dao():
    favourite_movie_dao = FavouriteMovieDAO(None)

    test_favourite_movie1 = FavouriteMovie(
        user_id=1,
        user='user1',
        movie_id=1,
        movie='movie1'
    )

    favourite_movie_dao.get_by_user_movie_id = MagicMock(return_value=test_favourite_movie1)
    favourite_movie_dao.create = MagicMock(return_value=FavouriteMovie(
        user_id=2,
        user='user2',
        movie_id=2,
        movie='movie2'
    ))
    favourite_movie_dao.delete = MagicMock()

    return favourite_movie_dao