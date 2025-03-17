from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_name = input()
    global_init(db_name)
    session = create_session()
    # app.run()
    for job in session.query(Job).all():
        if job.work_size < 20 and job.is_finished == 0:
            print(job)


if __name__ == '__main__':
    main()
