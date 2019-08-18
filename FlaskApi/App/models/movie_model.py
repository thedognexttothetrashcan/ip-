from App.ext import db
from App.models.base import TeachBaseModel


class Movie(TeachBaseModel):

    m_name = db.Column(db.String(64))
    m_duration = db.Column(db.Integer, default=90)