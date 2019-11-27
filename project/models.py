
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()
class User(db.Model,UserMixin):
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key = True)
   firstname = db.Column(db.String(100),nullable=True)
   lastname = db.Column(db.String(20),unique=True,nullable=False)
   email = db.Column(db.String(120),unique=True,nullable=False)
   password = db.Column(db.String(60),nullable=True)
   courses = db.relationship('Course', backref='Teacher', lazy=True)

   def __repr__(self):
        return f"User('{self.username},{self.id}')"

class Course(db.Model):
    id = db.Column('course_id',db.Integer,primary_key=True)
    name= db.Column(db.String(100),unique=True,nullable=False)
    students = db.relationship('Student', backref='Student', lazy=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)


class Student(db.Model):
    first_name = db.Column(db.String(100),nullable=True)
    last_name = db.Column(db.String(100),nullable=True)
    id = db.Column('student_id',db.Integer,primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'),nullable=False)
    homework = db.Column(db.Integer,nullable=True)
    midterm = db.Column(db.Integer,nullable=True)
    final = db.Column(db.Integer,nullable=True)
    average= db.Column(db.Integer,nullable=True)
