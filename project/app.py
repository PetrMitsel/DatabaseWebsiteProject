from flask import Flask,request,render_template,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from models import User,db,Course,Student
from forms import RegistrationForm,AddClassForm,AddStudentForm
from flask_login import login_user,current_user,logout_user,login_required,LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db.init_app(app)
bcrypt= Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category= 'info'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login")
def login():

    return render_template('login.html')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form= RegistrationForm ()
    if form.validate_on_submit():
       hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       user = User(firstname=form.firstname.data,lastname=form.lastname.data,password=hashed_password)
       db.session.add(user)
       db.session.commit()
       flash('Account succesfully created.','success')
       return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.route("/myclasses")
def myclasses():
    addstudentform = AddStudentForm ();
    addclassform = AddClassForm ();
    if(addclassform.validate_on_submit()):
        addclasses(addclassform.class_name.data)
    if(addstudentform.validate_on_submit()):
        addstudents()
    return render_template('myclasses.html',addclassform=addclassform,addstudentform=addstudentform)


def addStudents(Student):
    return

def addclasses(String):
    user=current_user
    course = Course(class_name=form.class_name.data,teacher_id=user.id)
    db.session.add(course)
    db.session.commit()

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
