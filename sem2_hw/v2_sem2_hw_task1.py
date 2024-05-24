# Задание №9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

import secrets
from flask import Flask, render_template, request, redirect, make_response, session, url_for

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def index():
    return render_template('index_2.html')


@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        session['user_name'] = request.form.get('user_name', 'email')
        return redirect(url_for('index'))
    return render_template('registration.html')


@app.route('/logout/')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
