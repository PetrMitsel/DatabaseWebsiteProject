from flask import Flask,request,render_template,url_for,redirect,flash,session
from flask_sqlalchemy import SQLAlchemy
from project.models import User,Course,Student
from project import db,app,bcrypt
from project.forms import RegistrationForm,AddClassForm,AddStudentForm,LoginForm
from flask_login import login_user,current_user,logout_user,login_required,LoginManager
import os
import sys
import statistics



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login",methods=['GET','POST'])
def login():
    form= LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check email and Password','danger')
    return render_template('login.html',form=form)

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form= RegistrationForm ()
    if form.validate_on_submit():
       hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       new_user = User(firstname=form.first_name.data,lastname=form.last_name.data,email=form.email.data,password=hashed_password)
       db.session.add(new_user)
       db.session.commit()
       flash('Account succesfully created.','success')
       print('Hello world!', file=sys.stderr)
       return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/myclasses",methods=['GET','POST'])
@login_required
def myclasses():
    courses= getcourses()
    addstudentform = AddStudentForm ();
    addclassform = AddClassForm ();
    
    if addclassform.submitclass.data and addclassform.validate_on_submit():
        addclasses(addclassform.class_name.data,current_user)
        return redirect(url_for('myclasses'))

    return render_template('myclasses.html',addclassform=addclassform,addstudentform=addstudentform,courses=courses)


@app.route("/addstudent",methods=['GET','POST'])
@login_required
def addstudent():

    courses= getcourses()
    addstudentform = AddStudentForm ();
    addclassform = AddClassForm ();
    print(bool(addstudentform.validate_on_submit()),file=sys.stderr)

    if addstudentform.validate_on_submit():
        grades= [addstudentform.homework.data,addstudentform.midterm.data,addstudentform.final.data]
        student = Student(first_name=addstudentform.students_first_name.data,last_name=addstudentform.students_last_name.data,Course=addstudentform.student_class.data,
        homework=addstudentform.homework.data,midterm=addstudentform.midterm.data,final=addstudentform.final.data,average=statistics.mean(grades))
        print(student.first_name, file=sys.stderr)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('myclasses'))

    return render_template('addstudent.html',addclassform=addclassform,addstudentform=addstudentform,courses=courses)

def addclasses(s,user):
    
    course = Course(name=s,Teacher=user)
    db.session.add(course)
    db.session.commit()

def getcourses():
    courses= Course.query.filter_by(Teacher=current_user).all()
    return courses

def makechoices(courses):
    coursenames = []
    students = []
    for course in courses:
        coursenames.append(course.name)
        students.append(course.students)
    #print(students, file=sys.stderr)      
    choices= zip(courses,coursenames)
    choices= set(choices)
    return choices

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
