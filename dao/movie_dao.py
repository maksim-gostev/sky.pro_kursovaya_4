from sqlalchemy import desc

from dao.base import BaseDAO
from dao.model.movie import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie


    def get_all_paginate(self, page, per_page):
        return self.session.query(Movie).paginate(page=page, per_page=per_page).items

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_new(self):
        return self.session.query(Movie).order_by(desc(Movie.year)).all()

    def get_by_year_paginate(self, page, per_page):
        return self.session.query(Movie).order_by(desc(Movie.year)).paginate(page=page, per_page=per_page).items
