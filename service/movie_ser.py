from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_by_id(bid)

    def get_all(self, filters: dict) -> MovieDAO:
        """
        Get all movies with filters
        """
        # if filters.get("status") == "new" and filters.get("page") is not None:
        #     movies = self.dao.get_by_year_paginate(page=int(filters.get("page")), per_page=12)
        if filters.get("status") == "new":
            movies = self.dao.get_by_new()
        # elif filters.get("page") is not None:
        #     movies = self.dao.get_all_paginate(page=int(filters.get("page")), per_page=12)
        else:
            movies = self.dao.get_all()
        return movies

