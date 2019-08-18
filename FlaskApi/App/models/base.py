from App.ext import db


class TeachBaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)

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
