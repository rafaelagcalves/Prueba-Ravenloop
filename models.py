from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, Date, Time, Float

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR, unique=True)
    password = db.Column(db.VARCHAR)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'User {self.username}'

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.username,
            "is_admin": self.is_admin
        }


class Files(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR)
    date = db.Column(db.Date)
    size = db.Column(db.VARCHAR)
    hash = db.Column(db.text)


    def __repr__(self):
        return f'Files {self.username}'

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "data": self.data,
            "size": self.size,
            "hash": self.hash
        }

