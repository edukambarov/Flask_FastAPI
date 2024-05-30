# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template

from task_2.model import db, Author, Book, BookAuthor

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)
@app.route('/')
def index():
    return f'Hello!'

@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')

# @app.cli.command('fill_tables')
# def fill_tables():
#     authors = []
#     author_1 = Author(firstname="Лев",
#                     lastname="Толстой")
#     db.session.add(author_1)
#     authors.append(author_1)
#     author_2 = Author(firstname="Александр",
#                       lastname="Пушкин")
#     db.session.add(author_2)
#     authors.append(author_2)
#     book_1 = Book(title = 'Пиковая дама',
#                     year = 1999,
#                     count = 3,
#                     author = authors[1])
#     db.session.add(book_1)
#     book_2 = Book(title='Евгений Онегин',
#                     year=1998,
#                     count=4,
#                     author=authors[1])
#     db.session.add(book_2)
#     book_3 = Book(title='Кавказский пленник',
#                     year=2002,
#                     count=2,
#                     author=authors[0])
#     db.session.add(book_3)
#     book_4 = Book(title='Воскресенье',
#                     year=2000,
#                     count=1,
#                     author=authors[0])
#     db.session.add(book_4)
#     db.session.commit()
#     print('Database is filled with data now.')

@app.route('/books/')
def students():
    books = Book.query.all()
    context = {'books': books}
    return render_template('registration.html', **context)





