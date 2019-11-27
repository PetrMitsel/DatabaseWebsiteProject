from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,EqualTo,Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),Length(min=4)])
    password=PasswordField('password',validators=[ InputRequired(),Length(min=4)])
    submit= SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password=PasswordField('Password', validators=[InputRequired()])
    confirm_password=PasswordField('Confirm Password', validators=[InputRequired(),EqualTo('password')])
    submit= SubmitField('Signup')

class AddStudentForm(FlaskForm):
    students_first_name = StringField('First Name', validators=[InputRequired()])
    students_last_name =StringField('Last Name', validators=[InputRequired()])
    student_class= StringField('Class',validators=[InputRequired()])
    submit= SubmitField('Add student')

class AddClassForm(FlaskForm):
    class_name = StringField('class name', validators=[InputRequired()])
    class_ID = StringField('class ID', validators=[InputRequired()])
    submit= SubmitField('Add class')
