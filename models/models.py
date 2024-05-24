import datetime
import sys
from importlib.resources import Resource
from Yoha import db
from sqlalchemy.dialects.postgresql import JSON


sys.path.append("D:\\Real time Projects")


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    confirm_password = db.Column(db.String(255), nullable=False)

    def __int__(self, user_name):
        self.User_name = user_name

    def __repr__(self):
        return f"<User {self.User_name}>"

class Demo_users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number