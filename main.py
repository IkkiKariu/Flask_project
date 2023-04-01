import flask
from flask import url_for

app = flask.Flask(__name__)

def get_tours():
    return {
        'Импор': {
            "country": "Импор",
            "description": "Пример описания места путешествия. Примера применрее ты ещё не видел. Этот прмерный пример наиболее непредвзятый и никаким образом не пытается влиять на формирование твого вкуса",
            "price": "38000K",
            "tour_name": "Тсункейдо",
            "img_path": "images/tsunkeido.png"
        },
        'Колечия': {
            "country": "Колечия",
            "description": "Пример описания места путешествия. Примера применрее ты ещё не видел. Этот прмерный пример наиболее непредвзятый и никаким образом не пытается влиять на формирование твого вкуса",
            "price": "84600K",
            "tour_name": "Ведор",
            "img_path": "images/vedor.png"
        },
        'Орбистан': {
            "country": "Орбистан",
            "description": "Пример описания места путешествия. Примера применрее ты ещё не видел. Этот прмерный пример наиболее непредвзятый и никаким образом не пытается влиять на формирование твого вкуса",
            "price": "17500K",
            "tour_name": "Лорндаз",
            "img_path": "images/lorndaz.png"
        },
        'Антегрия': {
            "country": "Антегрия",
            "description": "Пример описания места путешествия. Примера применрее ты ещё не видел. Этот прмерный пример наиболее непредвзятый и никаким образом не пытается влиять на формирование твого вкуса",
            "price": "37500K",
            "tour_name": "Аутер Грауз",
            "img_path": "images/antegria.png"
        },
        'Республия': {
            "country": "Республия",
            "description": "Пример описания места путешествия. Примера применрее ты ещё не видел. Этот прмерный пример наиболее непредвзятый и никаким образом не пытается влиять на формирование твого вкуса",
            "price": "26500K",
            "tour_name": "Бостан",
            "img_path": "images/bostan.jpg"
        },
        'Объединённая Федерация': {
            "country": "Объединённая Федерация",
            "description": "Пример описания места путешествия. Примера применрее ты ещё не видел. Этот прмерный пример наиболее непредвзятый и никаким образом не пытается влиять на формирование твого вкуса",
            "price": "47500K",
            "tour_name": "Грэйт Рапид",
            "img_path": "images/great_rapid.png"
        }
        }

@app.route('/')
def index():
    return flask.render_template('index.html', tours_page=url_for('tours'))


@app.route('/tours')
def tours():
    tours = get_tours()
    return flask.render_template('tours.html', tours=tours, index=url_for('index'))


@app.route('/<tour_name>')
def chosen_tour_view(tour_name):
    tours = get_tours()
    return flask.render_template('chosen_tour_page.html', tours=tours, c_tour_name=tour_name, index=url_for('index'), tours_page=url_for('tours'))


if __name__ == '__main__':
    app.run(debug=True)