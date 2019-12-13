from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField, SelectField, IntegerField
from wtforms.validators import InputRequired,EqualTo,Length,Email,NumberRange
from project.models import Course
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import current_user

def coursequery ():
    return Course.query.filter_by(Teacher=current_user)

def get_pk(obj):
    return str(obj)

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
    student_class= QuerySelectField(query_factory=coursequery,get_pk=get_pk)
    homework = IntegerField('Homework Grade',validators=[NumberRange(0,100)])
    midterm = IntegerField('Midterm Grade',validators=[NumberRange(0,100)])
    final = IntegerField('Final Grade',validators=[NumberRange(0,100)])
    submitstudent= SubmitField('Add Student')

class AddClassForm(FlaskForm):
    class_name = StringField('Course Name', validators=[InputRequired()])
    submitclass= SubmitField('Add Class')
