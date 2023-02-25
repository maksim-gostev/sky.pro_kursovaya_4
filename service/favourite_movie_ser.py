from dao.favourite_movie_dao import FavouriteMovieDAO

class FavouriteMovieService:
    def __init__(self, dao: FavouriteMovieDAO):
        self.dao = dao

    def create(self, data):
        return self.dao.create(data)


    def delete(self, mid, uid):
        return self.dao.delete(mid, uid)