import pytest

from service.director_ser import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_dy_id(self):
        director = self.director_service.get_by_id(1)
        assert director is not None
        assert director.id == 1
        assert director.name == "director1"


    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None
        assert len(directors) > 0