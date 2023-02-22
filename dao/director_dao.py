from dao.base import BaseDAO
from dao.model.director import Director


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director

    def get_all(self):
        return self.session.query(Director).all()


