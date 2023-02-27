from dao.model.favorite_movie import FavouriteMovie

class FavouriteMovieDAO:
    def __init__(self, session):
        self.session = session

    def get_by_user_movie_id(self, mid, uid):
        f_movie = self.session.query(FavouriteMovie).filter(FavouriteMovie.user_id == uid,
                                                            FavouriteMovie == mid).first()
        return f_movie


    def create(self, data):
        f_movie = FavouriteMovie(**data)
        self.session.add(f_movie)
        self.session.commit()
        return f_movie


    def delete(self, mid, uid):
        f_movie = self.get_by_user_movie_id(mid, uid)
        self.session.delete(f_movie)
        self.session.commit()