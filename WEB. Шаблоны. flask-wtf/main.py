from flask import Flask, url_for, render_template, redirect
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/<title>')
@app.route('/index')
@app.route('/index/<title>')
def index(title="Заготовка"):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/list_prof/<list>')
def list_prof(list):
    print(list)
    with open("list_prof.json", "rt", encoding="utf8") as f:
        jobs_list = json.loads(f.read())
    print(jobs_list)
    param = {}
    param['list'] = list
    param['jobs_list'] = jobs_list
    return render_template('list_prof.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['prof'] = prof
    return render_template('training.html', **param)


@app.route('/distribution')
def distribution():
    param = {}
    param['list'] = ['Катя', 'Саша', 'Ваня']
    return render_template('distribution.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман'
    param['sex'] = 'male'
    param['motivation'] = '-'
    param['ready'] = 'True'
    return render_template('auto_answer.html', **param)


class LoginForm(FlaskForm):
    id_astr = StringField('id астронавта', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('id астронавта', validators=[DataRequired()])
    password_cap = PasswordField('Пароль астронавта', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return f'<h1>Успешно!</h1>'


@app.route('/table/<sex>/<years>')
def table_param(sex, years):
    param = {}
    param['sex'] = sex
    param['years'] = int(years)
    return render_template('table_param.html', **param)


@app.route('/member')
def member():
    with open("templates/member.json", "rt", encoding="utf8") as f:
        jobs_list = json.loads(f.read())
    member = random.choice(list(jobs_list.keys()))
    param = {}
    param['member'] = jobs_list[member]
    param['job'] = ', '.join(sorted(jobs_list[member]['job']))
    print(jobs_list[member])
    return render_template('member.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
