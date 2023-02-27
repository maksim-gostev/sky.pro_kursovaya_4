import pytest

from service.movie_ser import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_dy_id(self):
        movie = self.movie_service.get_dy_id(1)
        assert movie.id == 1
        assert movie.title == 'title1'
        assert movie.description == 'description1'
        assert movie.trailer == 'trailer1'
        assert movie.year == 2001
        assert movie.rating == 1.0
        assert movie.genre_id == 1
        assert movie.genre == 'genre1'
        assert movie.director_id == 1
        assert movie.director == 'director1'

    def test_get_all(self):
        filters = {}
        movies = self.movie_service.get_all(filters)
        assert movies is not None
        assert len(movies) > 0

    def test_get_by_new(self):
        filters = {"status": "new"}
        movies = self.movie_service.get_all(filters)
        assert movies is not None
        assert len(movies) > 0



    def test_get_all_paginate(self):
        filters = {"page": 1}
        movies = self.movie_service.get_all(filters)
        assert movies is not None
        assert len(movies) > 0


    def test_get_by_year_paginate(self):
        filters = {"status": "new",
                   "page": 1}
        movies = self.movie_service.get_all(filters)
        assert movies is not None
        assert len(movies) > 0