from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import InputRequired,EqualTo,Length,Email 

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),Email()])
    password=PasswordField('Password',validators=[ InputRequired(),Length(min=4)])
    remember= BooleanField('Remember Me')
    submit= SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(),Email()])
    password=PasswordField('Password', validators=[InputRequired()])
    confirm_password=PasswordField('Confirm Password', validators=[InputRequired(),EqualTo('password')])
    submit= SubmitField('Signup')

class AddStudentForm(FlaskForm):
    students_first_name = StringField('First Name', validators=[InputRequired()])
    students_last_name =StringField('Last Name', validators=[InputRequired()])
    student_class= StringField('Class',validators=[InputRequired()])
    submit= SubmitField('Add Student')

class AddClassForm(FlaskForm):
    class_name = StringField('Course Name', validators=[InputRequired()])
    submit= SubmitField('Add Class')
