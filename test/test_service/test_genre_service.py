import pytest

from service.genre_ser import GenreService


class TestGetreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)


    def test_get_dy_id(self):
        genre = self.genre_service.get_dy_id(1)
        assert  genre is not None
        assert genre.id == 1
        assert genre.name == 'genre1'


    def test_get_all(self):
        genre = self.genre_service.get_all()
        assert genre is not None
        assert len(genre) > 0