from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,EqualTo,Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),Length(min=4)])
    password=PasswordField('password',validators=[ InputRequired(),Length(min=4)])
    submit= SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    first_name = StringField('first name', validators=[InputRequired()])
    last_name = StringField('last name', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired()])
    password=PasswordField('password', validators=[InputRequired()])
    confirm_password=PasswordField('confirm password', validators=[InputRequired(),EqualTo('password')])
    submit= SubmitField('Signup')

class AddStudentForm(FlaskForm):
    students_first_name = StringField('first name', validators=[InputRequired()])
    students_last_name =StringField('last name', validators=[InputRequired()])
    students_ID = StringField('student ID', validators=[InputRequired()])
    student_class= StringField('class',validators=[InputRequired()])
    submit= SubmitField('Add student')

class AddClass(FlaskForm):
    class_name = StringField('class name', validators=[InputRequired()])
    class_ID = StringField('class ID', validators=[InputRequired()])
    submit= SubmitField('Add class')





