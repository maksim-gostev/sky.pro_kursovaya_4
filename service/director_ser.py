from dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_by_id(self, bid):
        return self.dao.get_by_id(bid)

    def get_all(self):
        return self.dao.get_all()

