from project import login_manager, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=True)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    courses = db.relationship("Course", backref="Teacher", lazy=True)

    def __repr__(self):
        return f"User('{self.id},{self.email}')"


class Course(db.Model):
    id = db.Column("course_id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    students = db.relationship("Student", backref="Course", lazy=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    assignments = db.relationship("Assignment", backref="Course", lazy=True)

    def __repr__(self):
        return self.name


class Student(db.Model):

    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    id = db.Column("student_id", db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)
    grades = db.relationship("Grade", backref="Student", lazy=True)

    def __repr__(self):
        return f"{self.first_name},{self.last_name}"


class Grade(db.Model):

    id = db.Column("grade_id", db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    student_id = db.Column(
        db.Integer, db.ForeignKey("student.student_id"), nullable=False
    )
    assignment_id = db.Column(
        db.Integer, db.ForeignKey("assignment.assignment_id"), nullable=False
    )


class Assignment(db.Model):
    __tablename__ = "assignment"
    id = db.Column("assignment_id", db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    assignment_name = db.Column(db.String(100), nullable=True)
    # grades = db.relationship("Grade", backref="Assignment", lazy=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"{self.assignment_name}"
