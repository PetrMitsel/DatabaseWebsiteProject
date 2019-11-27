from flask_wtf import FlaskForm
from wtforms import StringField, Passwordfield, ConfirmPasswordField, Emailfield, FirstNamefield, LastNamefield, StudentsFirstNamefield,StudentsLastNamefield,StudentsIDfield,StudentsClassfield,ClassNamefield,ClassIDfield
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),Length(min=4)])
    password=Passwordfield('password'validators=[ InputRequired(),Length(min=4)])
    submit= SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    first_name = FirstNamefield('first name', validators=[InputRequired()])
    last_name = LastNamefield('last name', validators=[InputRequired()])
    email = Emailfield('email', validators=[InputRequired()])
    password=Passwordfield('password', validators=[InputRequired()])
    confirm_password=ConfirmPasswordField('confirm password', validators=[InputRequired(),EqualTo('password')])
    submit= SubmitField('Signup')

class AddStudentForm(FlaskForm):
    students_first_name = StudentsFirstNamefield('first name', validators=[InputRequired()])
    students_last_name = StudentsLastNamefield('last name', validators=[InputRequired()])
    students_ID = StudentsIDfield('student ID', validators=[InputRequired()])
    student_class= StudentsClassfield('class',validators=[InputRequired()])
    submit= SubmitField('Add student')

class AddClass(FlaskForm):
    class_name = ClassNamefield('class name', validators=[InputRequired()])
    class_ID = ClassIDfield('class ID', validators=[InputRequired()])
    submit= SubmitField('Add class')





