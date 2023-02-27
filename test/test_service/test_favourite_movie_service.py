import pytest

from service.favourite_movie_ser import FavouriteMovieService


class TestFavouriteMovieService:
    @pytest.fixture(autouse=True)
    def favourite_movie_service(self, favourite_movie_dao):
        self.favourite_movie_service = FavouriteMovieService(favourite_movie_dao)

    def test_create(self):
        data = {
            'user_id': 2,
            'user': 'user2',
            'movie_id': 2,
            'movie': 'movie2'
        }
        f_movie = self.favourite_movie_service.create(data)
        assert f_movie is not None
        assert f_movie.user_id == 2
        assert f_movie.user == 'user2'
        assert f_movie.movie_id == 2
        assert f_movie.movie == 'movie2'



