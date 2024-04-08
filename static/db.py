from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # создаем объект базы данных

class User(db.Model): # создаем модель пользователя,
    id =db.Column(db.Integer, primary_key=True) # первичный ключ таблицы пользователей
    username = db.Column(db.String(80), unique=True, nullable=False) # имя пользователя
    lastname = db.Column(db.String(80), unique=True, nullable=False) # фамилия пользователя
    email = db.Column(db.String(120), unique=True, nullable=False) # электронная почта
    password = db.Column(db.String(120), nullable=False) # пароль пользователя
    active = db.Column(db.Boolean, default=True) # активность пользователя

    def __repr__(self):
        return f'User({self.username}, {self.email})'

