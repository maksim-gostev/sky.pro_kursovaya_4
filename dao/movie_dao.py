from sqlalchemy import desc

from dao.base import BaseDAO
from dao.model.movie import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie


    def get_all(self, filters):
        t = self.session.query(Movie)
        if filters["status"] == "new":
            t = t.order_by(desc(Movie.year))
        if filters["page"] is not None:
            t = t.paginate(page=int(filters["page"]), per_page=12)
        return t.all()

