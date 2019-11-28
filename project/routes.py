from flask import Flask,request,render_template,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from project.models import User,Course,Student
from project import db,app,bcrypt
from project.forms import RegistrationForm,AddClassForm,AddStudentForm,LoginForm
from flask_login import login_user,current_user,logout_user,login_required,LoginManager
import os
import sys



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


@app.route("/myclasses")
def myclasses():
    addstudentform = AddStudentForm ();
    addclassform = AddClassForm ();
    if(addclassform.validate_on_submit()):
        addclasses(addclassform.class_name.data)
    if(addstudentform.validate_on_submit()):
        addStudents(addstudentform.student_class.data)
    return render_template('myclasses.html',addclassform=addclassform,addstudentform=addstudentform)


def addStudents(Student):
    student = Student()
    db.session.add()
    db.session.commit()



def addclasses(s):
    user=current_user
    course = Course(class_name=s,teacher_id=user.teacher_id)
    db.session.add(course)
    db.session.commit()

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
