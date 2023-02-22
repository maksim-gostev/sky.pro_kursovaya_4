from marshmallow import Schema, fields

from dao.model.models_main import Base
from setup_db import db


class Director(Base):
    __tablename__ = 'director'

    name = db.Column(db.String(255), nullable=False, unique=True)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
