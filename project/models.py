
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()
class User(db.Model,UserMixin):
   id = db.Column('teacher_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100),nullable=True)
   username = db.Column(db.String(20),unique=True,nullable=False)
   email = db.Column(db.String(120),unique=True,nullable=False)
   password = db.Column(db.String(60),nullable=True)
   courses = db.relationship('Course', backref='Coursetaught', lazy=True)
   
   def __repr__(self):
        return f"User('{self.username},{self.email}')"

class Course(db.Model):
    id = db.Column('course_id',db.Integer,primary_key=True)
    name= db.Column(db.String(100),unique=True,nullable=False)
    students = db.relationship('Student', backref='Student', lazy=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('User.id'),nullable=False)


class Student(db.Model):
    name = db.Column(db.String(100),nullable=True)
    id = db.Column('student_id',db.Integer,primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('Course.id'),nullable=False)
