from dao.base import BaseDAO
from dao.model.genre import Genre



class GenreDAO(BaseDAO[Genre]):
    __model__ = Genre

    def get_all(self):
        return self.session.query(Genre).all()

