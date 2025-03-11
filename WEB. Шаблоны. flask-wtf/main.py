from flask import Flask, url_for, render_template
import json

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
