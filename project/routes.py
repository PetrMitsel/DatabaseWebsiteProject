from flask import Flask, request, render_template, url_for, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_table import Col, Table
from project.models import User, Course, Student, Grade, Assignment
from project import db, app, bcrypt
from project.tables import CourseTable
from project.forms import (
    RegistrationForm,
    AddClassForm,
    AddStudentForm,
    LoginForm,
    AddAssignmentForm,
    AddGradesForm,
)
from flask_login import (
    login_user,
    current_user,
    logout_user,
    login_required,
    LoginManager,
)
import os
import sys
import statistics


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccesful. Please check email and Password", "danger")
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        new_user = User(
            firstname=form.first_name.data,
            lastname=form.last_name.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Account succesfully created.", "success")
        print("Hello world!", file=sys.stderr)
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user = current_user
    return render_template("profile.html", user=current_user, courses=getcourses())


"""
course detail
"""


@app.route("/course/<course_id>", methods=["GET", "POST"])
@login_required
def course_detail(course_id):
    course = Course.query.filter_by(id=course_id).first()
    addstudentform = AddStudentForm()

    addassignment_form = AddAssignmentForm()

    addgrades_form = AddGradesForm()
    addgrades_form.course_id = course_id
    addgrades_form.student.query = Student.query.filter_by(course_id=course_id)
    addgrades_form.assignment.query = Assignment.query.filter_by(course_id=course_id)

    students = Student.query.filter_by(course_id=course_id).all()
    assignments = Assignment.query.filter_by(course_id=course_id)
    course_table = CourseTable(students)

    # for assignment in assignments:
    #     for i in range(len(students) - 1):
    #         student = students[i]
    #         assignment_name = assignment.assignment_name
    #         course_table.add_column(student.grades[i], Col(assignment_name))

    if addstudentform.submitstudent.data and addstudentform.validate_on_submit():

        student = Student(
            first_name=addstudentform.students_first_name.data,
            last_name=addstudentform.students_last_name.data,
            course_id=course_id,
        )
        db.session.add(student)
        db.session.commit()
    if addgrades_form.submit_grade.data and addgrades_form.validate_on_submit():

        grade = Grade(
            value=addgrades_form.value.data,
            student_id=addgrades_form.student.data.id,
            assignment_id=addgrades_form.assignment.data.id,
        )
        db.session.add(grade)
        db.session.commit()
    if (
        addassignment_form.submit_assignment.data
        and addassignment_form.validate_on_submit()
    ):
        assignment = Assignment(
            assignment_name=addassignment_form.assignment_name.data,
            description=addassignment_form.assignment_description.data,
            course_id=course_id,
            weight=addassignment_form.weight.data,
        )
        db.session.add(assignment)
        db.session.commit()

    return render_template(
        "course_detail.html",
        user=current_user,
        course=course,
        addstudentform=addstudentform,
        addgrades_form=addgrades_form,
        addassignment_form=addassignment_form,
        table=course_table,
    )


@app.route("/myclasses", methods=["GET", "POST"])
@login_required
def myclasses():
    courses = getcourses()
    addclassform = AddClassForm()

    if addclassform.submitclass.data and addclassform.validate_on_submit():
        addclasses(addclassform.class_name.data, current_user)
        # return redirect(url_for("myclasses"))

    return render_template(
        "myclasses.html", addclassform=addclassform, courses=courses,
    )


# factor out table into course_detail
# add grade,assignment and student are limited to course detail.
# My classes should be redundant over profile, or have limited info


def addclasses(s, user):

    course = Course(name=s, Teacher=user)
    db.session.add(course)
    db.session.commit()


def getcourses():
    courses = Course.query.filter_by(Teacher=current_user).all()
    return courses


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
