from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    SelectField,
    IntegerField,
)
from wtforms.validators import (
    InputRequired,
    EqualTo,
    Length,
    Email,
    NumberRange,
    ValidationError,
)
from project.models import Course, Student
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import current_user


def coursequery():
    return Course.query.filter_by(Teacher=current_user)


def get_pk(obj):
    return str(obj)


def validate_name(form, field):
    if len(field.data) > 20:
        raise ValidationError("Name must be between 1 and 20 characters")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign in")


class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Signup")


class AddStudentForm(FlaskForm):
    students_first_name = StringField(
        "First Name", validators=[InputRequired(), validate_name]
    )
    students_last_name = StringField(
        "Last Name", validators=[InputRequired(), validate_name]
    )
    # student_class = QuerySelectField(query_factory=coursequery, get_pk=get_pk)
    submitstudent = SubmitField("Add Student")


class AddClassForm(FlaskForm):
    class_name = StringField("Course Name", validators=[InputRequired()])
    submitclass = SubmitField("Add Class")


class AddGradesForm(FlaskForm):
    course_id = 0
    student_id = 0
    value = IntegerField("Grade", validators=[InputRequired(), NumberRange(0, 100)])
    student = QuerySelectField(get_pk=get_pk)
    assignment = QuerySelectField(get_pk=get_pk)
    submit_grade = SubmitField("Add Grade")


class AddAssignmentForm(FlaskForm):
    assignment_name = StringField(
        "Assignment Name", validators=[InputRequired(), validate_name]
    )
    assignment_description = StringField(
        "Assignment Description", validators=[InputRequired()]
    )
    weight = IntegerField("Weight", validators=[InputRequired(), NumberRange(0, 100)])
    submit_assignment = SubmitField("Add Assignment")
