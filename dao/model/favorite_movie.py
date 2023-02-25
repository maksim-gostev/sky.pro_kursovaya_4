from marshmallow import Schema, fields

from setup_db import db

class FavouriteMovie(db.Model):
    __tablename__ = "favourite_movie"

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), primary_key=True)
    movie = db.relationship("Movie")


class FavouriteMovieSchema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()