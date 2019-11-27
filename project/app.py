from flask import Flask,request,render_template,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from models import User,db
from forms import RegistrationForm
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
       new_user = User(firstname=form.first_name.data,lastname=form.last_name.data,email=form.email.data,password=hashed_password)
       db.session.add(new_user)
       db.session.commit()
       flash('Account succesfully created.','success')
       return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.route("/myclasses")
def myclasses():

    return render_template('myclasses.html')




if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)