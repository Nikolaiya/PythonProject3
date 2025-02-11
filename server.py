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


@app.route('/image_sample')
def return_sample_page():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='image_mars/img.jpeg')}" alt="здесь должна была быть картинка, но не нашлась">
                      </body>
                    </html>"""

@app.route('/promotion_image')
def return_promotion_image():
    k = []
    i = 0
    while True:
        if i == 0:
            k.append('<h2>Человечество вырастает из детства.</h2></br>')
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

    promotion_text = ''.join(k)

    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='image_mars/img.png')}" alt="здесь должна была быть картинка, но не нашлась">
                    <div>{promotion_text}</div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=9000, host='127.0.0.1')
