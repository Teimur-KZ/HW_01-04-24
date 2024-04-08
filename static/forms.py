from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

'''wtforms - библиотека для создания форм в Flask'''
'''StringField - строковое поле'''
'''PasswordField - поле для ввода пароля'''

from wtforms.validators import DataRequired, Length, EqualTo, Email
'''DataRequired - валидатор, который проверяет, что поле не пустое'''
'''Length - валидатор, который проверяет, что длина поля находится в определенных пределах'''
'''EqualTo - валидатор, который проверяет, что значение поля равно значению другого поля'''
'''Email - валидатор, который проверяет, что поле содержит корректный email'''

class RegistrationForm(FlaskForm):
    '''Класс формы для регистрации'''
    username = StringField('Ваше Имя:', validators=[DataRequired()])
    lastname = StringField('Ваша Фамилия:', validators=[DataRequired()])
    email = StringField('Ваш Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль:', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Повторите пароль:', validators=[DataRequired(), EqualTo('password')])

class LoginForm(FlaskForm):
    '''Класс формы для входа'''
    username = StringField('Ввидите Имя:', validators=[DataRequired()])
    password = PasswordField('Ввидите Пароль:', validators=[DataRequired()])