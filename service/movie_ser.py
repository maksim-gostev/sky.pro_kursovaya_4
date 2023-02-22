from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_by_id(bid)

    def get_all(self, filters):
        return self.dao.get_all(filters)


