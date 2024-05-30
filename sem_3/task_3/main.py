# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

from flask import Flask, render_template

from task_1.model import db, Student, Faculty

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
@app.route('/')
def index():
    return f'Hello!'

@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')

@app.cli.command('fill_tables')
def fill_tables():
    count = 5
    for i in range(1, count + 1):
        new_faculty = Faculty(name=f'Faculty {i}')
        db.session.add(new_faculty)
        for j in range(1, count + 1):
            new_student = Student(firstname=f'Student_{j*10+i}',
                                lastname=f'Student_{i*10+j}',
                                age=17+j,
                                gender='male',
                                group=i*10+j,
                                faculty_id=i)

            db.session.add(new_student)
    db.session.commit()
    print('Database is filled with data now.')

@app.route('/students/')
def students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)





