# Задание №4
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных.
# Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.


# Задание №6
# Дополняем прошлую задачу
# Создайте форму для регистрации пользователей в вашем
# веб-приложении.
# Форма должна содержать следующие поля: имя
# пользователя, электронная почта, пароль и подтверждение
# пароля.
# Все поля обязательны для заполнения, и электронная почта
# должна быть валидным адресом.
# После отправки формы, выведите успешное сообщение об
# успешной регистрации.

# Задание №7
# Создайте форму регистрации пользователей в приложении Flask. Форма должна
# содержать поля: имя, фамилия, email, пароль и подтверждение пароля. При отправке
# формы данные должны валидироваться на следующие условия:
# ○ Все поля обязательны для заполнения.
# ○ Поле email должно быть валидным email адресом.
# ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и
# одну цифру.
# ○ Поле подтверждения пароля должно совпадать с полем пароля.
# ○ Если данные формы не прошли валидацию, на странице должна быть выведена
# соответствующая ошибка.
# ○ Если данные формы прошли валидацию, на странице должно быть выведено
# сообщение об успешной регистрации.


# Задание №8
# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован.


from flask import Flask, render_template, request
from sem3_hw.forms import RegisterForm
from sem3_hw.model import db, User
from flask_wtf.csrf import CSRFProtect
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('main.html')

@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')

@app.route('/registration/', methods=['GET','POST'])
def registration():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Обработка(хэширование) пароля
        h = hashlib.md5(password.encode(encoding='UTF-8', errors='strict'))
        p = h.hexdigest()
        user = User(name=name,
                    email=email,
                    password=p)
        # Отправка данных о пользователе в БД с уже захэшированным паролем
        db.session.add(user)
        db.session.commit()
    return render_template('registration.html', form=form)








