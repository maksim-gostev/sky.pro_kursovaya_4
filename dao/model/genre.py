from marshmallow import Schema, fields

from dao.model.models_main import Base
from setup_db import db


class Genre(Base):
    __tablename__ = 'genre'

    name = db.Column(db.String(255), nullable=False, unique=True)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
