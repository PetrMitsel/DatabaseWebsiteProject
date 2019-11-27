from flask import Flask,request,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

#import dbconfig

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db = SQLAlchemy(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login")
def login():

    return render_template('login.html')

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method== 'POST':
        first_name=request.form['f-name']
        last_name=request.form['l-name']
        email=request.form['email']
        password=request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO Users (teacher_firstname,teacher_lastname,teacher_email,teacher_password) 
        VALUES (%s,%s,%s,%s)''',(first_name,last_name,email,password))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('myclasses'))
    return render_template('register.html')


@app.route("/myclasses")
def myclasses():
    return render_template('myclasses.html')




if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)