from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, validators
from wtforms.validators import DataRequired, EqualTo, Email, Length


def custom_validator(form, field):
    splitted = [ch for ch in field.data]
    for ch in splitted:
        if ch.isdigit():
            splitted.remove(ch)
            break
    else:
        raise validators.ValidationError('Password must consist at least 1 letter and 1 digit')
    for ch in splitted:
        if ch.isalpha():
            break
    else:
        raise validators.ValidationError('Password must consist at least 1 letter and 1 digit')
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8),
                                                     custom_validator])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password')])

