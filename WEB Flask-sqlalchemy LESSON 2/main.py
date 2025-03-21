from flask import Flask
from data import db_session
from data.users import User
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    pass


if __name__ == '__main__':
    main()
