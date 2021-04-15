from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    email_field = EmailField('Логин/Адрес электронной почты', validators=[DataRequired()])
    password_field = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password_field = PasswordField('Повторить пароль', validators=[EqualTo('password_field')])
    surname_field = StringField('Фамилия', validators=[DataRequired()])
    name_field = StringField('Имя', validators=[DataRequired()])
    age_field = IntegerField('Возраст', validators=[DataRequired()])
    position_field = StringField('Должность', validators=[DataRequired()])
    speciality_field = StringField('Специальность', validators=[DataRequired()])
    address_field = StringField('Адрес', validators=[DataRequired()])
    submit_field = SubmitField('Подтвердить')
