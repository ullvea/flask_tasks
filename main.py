from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def index1():
    return "Миссия Колонизация Марса!"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!!"


@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства.',

                      'Человечеству мала одна планета.',

                      'Мы сделаем обитаемыми безжизненные пока планеты.',

                      'И начнем с Марса!',

                      'Присоединяйся!']
    return '</br>'.join(countdown_list)


@app.route('/')
@app.route('/image_mars')
def image_mars():
    return '''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet" 
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                       crossorigin="anonymous">
                       <title>Привет, Марс!</title>
                     </head>
                     <body>
                       <h1>Жди нас, Марс!</h1>
                       <img src="/static/image_mars/MARS.png"
                       <p>
                       <h6>Вот она какая, красная планета.</h6>
                       </p>
                     </body>
                   </html>'''


@app.route('/')
@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet" 
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                       crossorigin="anonymous">
                       <title>Колонизация</title>
                     </head>
                     <body>
                       <link rel="stylesheet" href="static/css/style.css">
                       <h1>Жди нас, Марс!</h1>
                       <img src="/static/image_mars/MARS.png"
                       <p>
                       <div class="alert alert-secondary" role="alert">
                       </br>Человечество вырастает из детства.</div>
                       <div class="alert alert-success" role="alert">
                       </br>Человечеству мала одна планета.</div>
                       <div class="alert alert-secondary" role="alert">
                       </br>Мы сделаем обитаемыми безжизненные пока планеты.</div>
                       <div class="alert alert-warning" role="alert">
                       </br>И начнем с Марса!</div>
                       <div class="alert alert-danger" role="alert">
                       </br>Присоединяйся!</div>
                       </p>
                     </body>
                   </html>'''

@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet" 
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                       crossorigin="anonymous">
                       <title>Варианты выбора</title>
                     </head>
                     <body>
                       <h1>Мое предложение:{planet_name}</h1>
                       <h2>Эта планета близка к Земле;</h2>
                       <p>
                       <h2>
                       <div class="alert alert-success" role="alert">
                       </br>На ней много необходимых ресурсов;</div>
                       <div class="alert alert-secondary" role="alert">
                       </br>На ней есть вода и атмосфера;</div>
                       <div class="alert alert-warning" role="alert">
                       </br>На ней есть небольшое магнитное поле;</div>
                       <div class="alert alert-danger" role="alert">
                       </br>Наконец, она просто красива!</div>
                       </p>
                     </body>
                   </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet" 
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                       crossorigin="anonymous">
                       <title>Результаты</title>
                     </head>
                     <body>
                       <h1>Результаты отбора</h1>
                       <h2>Претендента на участие в миссии {nickname}:</h2>
                       <p>
                       <h2>
                       <div class="alert alert-success" role="alert">
                       </br>Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
                       </br>составляет {rating}!</div>
                       <div class="alert alert-warning" role="alert">
                       </br>Желаем удачи!</div>

                       </p>
                     </body>
                   </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                       <html lang="en">
                         <head>
                           <meta charset="utf-8">
                           <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet" 
                           href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                           integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                           crossorigin="anonymous">
                           <title>Пейзажи Mарса</title>
                         </head>
                         <body>
                            <div align="center">
                           <h1>Пейзажи Марса</h1>
                           
                         </body>
                       </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
