from dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_by_id(bid)

    def get_all(self):
        return self.dao.get_all()


