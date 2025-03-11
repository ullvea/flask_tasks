from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<title>')
@app.route('/index')
@app.route('/index/<title>')
def index(title="Заготовка"):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


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
                           <div id="carouselExampleIndicators" class="carousel slide carousel-fade" data-ride="carousel">
                              <ol class="carousel-indicators">
                                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                              </ol>
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img src="static/landscapes/image1.jpg" class="d-block w-100" alt="image1">
                                </div>
                                <div class="carousel-item">
                                  <img src="static/landscapes/image2.jpg" class="d-block w-100" alt="image2">
                                </div>
                                <div class="carousel-item">
                                  <img src="static/landscapes/image3.jpg" class="d-block w-100" alt="image3">
                                </div>
                              </div>
                              <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
                            </body>
                          </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
