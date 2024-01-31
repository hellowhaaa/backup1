from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Regexp, ValidationError,Email,
                                Length, EqualTo)

from models import User

def name_exists(form, field):
    # the form is running on! the field which is username is running too
    if User.select().where(User.username == field.data).exists():
        # return True or False
        raise ValueError('User with that name already exists.')
    
def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        # return True or False
        raise ValueError('User with that email already exists.')


class RegisterForm(Form):
    # StringField(第一個argu 是label!!!!)
    username = StringField(
        'Username',
        validators = [
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message = ("Username should be one word, letters, numbers andunderscore only")
            ),
            name_exists
            # our own validator
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Password must match!')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired()]
    )

class LoginForm(Form):
    email = StringField(
    'Email',
    validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField(
    'Password',
    validators=[
        DataRequired()
    ])