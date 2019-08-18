from App.ext import db
from App.utils import BaseModel


class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16), unique=True)


class Movie(BaseModel,db.Model):
    m_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    m_name = db.Column(db.String(64))
    m_duration = db.Column(db.Integer, default=90)

    def to_dict(self):
        return {"m_name": self.m_name, "m_duration": self.m_duration, "m_id": self.m_id}


class TeachBaseModel(db.Model):
    __abstract__ = True

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False


class Blog(TeachBaseModel):
    b_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    b_content = db.Column(db.String(255))