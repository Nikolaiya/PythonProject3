from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def no_index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    k = []
    i = 0
    while True:
        if i == 0:
            k.append('Человечество вырастает из детства.</br>')
            i += 1
        elif i == 1:
            k.append('Человечеству мала одна планета.</br>')
            i += 1
        elif i == 2:
            k.append('Мы сделаем обитаемыми безжизненные пока планеты.</br>')
            i += 1
        elif i == 3:
            k.append('И начнем с Марса!</br>')
            i += 1
        elif i == 4:
            k.append('Присоединяйся!')
            break
        else:
            break
    return ''.join(k)


if __name__ == '__main__':
    app.run(port=9000, host='127.0.0.1')
