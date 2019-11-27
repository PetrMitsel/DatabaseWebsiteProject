from app import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

class User(db.Model,UserMixin):
   id = db.Column('teacher_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100),nullable=True)
   username = db.Column(db.String(20),unique=True,nullable=False)
   email = db.Column(db.String(120),unique=True,nullable=False)
   password = db.Column(db.String(60),nullable=True)
   
   def __repr__(self):
        return f"User('{self.username},{self.email}')"

class Course(db.Model):
    id = db.Column('course_id',db.Integer,primary_key=True)
    name= db.Column(db.String(100),unique=True,nullable=False)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
