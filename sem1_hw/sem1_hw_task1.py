from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def main_page():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)

@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    clothes_items = [{'text': 'Сине-белая рубашка в клетку', 'image': 'clothes1.jpg'},
                   {'text': 'Чёрная рубашка', 'image': 'clothes2.jpg'},
                   {'text': 'Красная рубашка', 'image': 'clothes3.jpg'}, ]
    return render_template('clothes.html', **context, clothes=clothes_items)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    shoes_items = [{'text': 'Чёрные туфли', 'image': 'shoes1.jpg'},
                    {'text': 'Коричневые лоуферы', 'image': 'shoes2.jpg'},
                    {'text': 'Коричневые туфли оксфорд', 'image': 'shoes3.jpg'}, ]
    return render_template('shoes.html', **context, shoes=shoes_items)


@app.route('/jackets/')
def jackets():
    context = {'title': 'Куртки'}
    jacket_items = [{'text': 'Куртка песчаного цвета', 'image': 'jacket1.jpg'},
                    {'text': 'Куртка чёрного цвета', 'image': 'jacket2.jpg'},
                    {'text': 'Куртка цвета хаки', 'image': 'jacket3.jpg'},]
    return render_template('jackets.html', **context, jackets=jacket_items)


if __name__ == '__main__':
    app.run(debug=True)


