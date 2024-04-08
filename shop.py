from flask import Flask, session, redirect, url_for, request, render_template
from flask_wtf.csrf import CSRFProtect
from static.forms import RegistrationForm, LoginForm
from static.db import db, User
from werkzeug.security import generate_password_hash

# Домашнее задание Урок 3. Погружение во Flask 01.04.24 начало:-------------------------------------
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    db.init_app(app)  # инициализирую db с приложением Flask

    with app.app_context():
        db.create_all()  # создаем все таблицы в базе данных

    return app

app = create_app()
app.secret_key = '76fa5b0ec1841105a24b3de3c66e3a49e26dea0a2bcedcff143fc7cc733d500f'
csrf = CSRFProtect(app)



@app.route('/register/', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    login_form = LoginForm()
    if request.method == 'POST' and register_form.validate():
        # если метод запроса POST и форма прошла валидацию
        username = register_form.username.data
        lastname = register_form.lastname.data
        email = register_form.email.data # получаем данные из поля email
        password = generate_password_hash(register_form.password.data) # получаем данные из поля password

        print(f'Email: {email}, Password: {password}')
        if username:
            session['username'] = username # добавляем имя пользователя в сессию
            new_user = User(username=username, lastname=lastname, email=email, password=password)  # создаем нового пользователя
            db.session.add(new_user)  # добавляем нового пользователя в сессию
            db.session.commit()  # сохраняем изменения
            return redirect(url_for('user_lk'))

    return render_template('form.html', register_form=register_form, login_form=login_form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    register_form = RegistrationForm()
    username = None
    if request.method == 'POST' and login_form.validate():
        # если метод запроса POST и форма прошла валидацию
        username = login_form.username.data # получаем данные из поля username
        password = generate_password_hash(login_form.password.data) # получаем данные из поля password
        if username:
            session['username'] = username
            return redirect(url_for('user_lk'))
    return render_template('form.html', register_form=register_form, login_form=login_form)

# Домашнее задание Урок 3. Погружение во Flask 01.04.24 конец:-------------------------------------










# Домашнее задание Урок 2. Погружение во Flask 28.03.24 начало:-------------------------------------

@app.route('/user_lk/')
def user_lk():
    if 'username' in session:
        context = {'title': 'Личный кабинет', 'text': 'Привет, ' + session['username'] + '!, <a href="/logout/">Выйти</a>'}
        return render_template('lk.html', **context)
    return redirect(url_for('login'))

'''
Для выхода из сессии используется метод pop() объекта session.
Этот метод удаляет значение по ключу из словаря. 
Ключ — username. 
После удаления значения, пользователь перенаправляется на страницу ввода имени и электронной почты.
'''
@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Домашнее задание Урок 2. Погружение во Flask 28.03.24 конец:-------------------------------------

@app.route('/') # декоратор маршрутизации запросов
def index():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это главная страница Интернет магазина</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашими товарами</p>')
    context = {'text': _text_info, 'title': 'Главная страница'}
    return render_template('index.html', **context)

@app.route('/about/') # декоратор маршрутизации запросов
def about():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница о нас</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете узнать о нас больше</p>')
    context = {'text': _text_info, 'title': 'О Нас'}
    return render_template('about.html', **context)

@app.route('/contacts/') # декоратор маршрутизации запросов
def contacts():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница контактов</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете связаться с нами</p>')
    context = {'text': _text_info, 'title': 'Контакты'}
    return render_template('contacts.html', **context)

@app.route('/cloth/') # декоратор маршрутизации запросов
def cloth():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница одежды</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашей одеждой</p>')
    context = {'text': _text_info, 'title': 'Одежда'}
    return render_template('cloth.html', **context)

@app.route('/shoes/') # декоратор маршрутизации запросов
def shoes():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница обуви</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашей обувью</p>')
    context = {'text': _text_info, 'title': 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/jacket/') # декоратор маршрутизации запросов
def jacket():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница курток</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашими куртками</p>')
    context = {'text': _text_info, 'title': 'Куртки'}
    return render_template('jacket.html', **context)

if __name__ == '__main__':
    app.run(debug=True) # запуск приложения
