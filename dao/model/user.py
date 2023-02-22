from marshmallow import Schema, fields

from dao.model.models_main import Base
from setup_db import db


class User(Base):
	__tablename__ = 'user'

	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	name = db.Column(db.String)
	surname = db.Column(db.String)
	favorite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))


class UserSchema(Schema):
	id = fields.Int()
	email = fields.Str()
	password = fields.Str()
	name = fields.Str()
	surname = fields.Str()
	favorite_genre = fields.Int()
