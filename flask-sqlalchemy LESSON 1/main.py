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
    for dep in session.query(Department).filter(Department.id == 1):
        for i in list(map(int, dep.members.split(', '))):
            sum_hours = 0
            for user in session.query(Jobs).filter(Jobs.collaborators.like(f'%{i}%')):
                sum_hours += user.work_size
            if sum_hours > 25:
                print(user.name, user.surname)


if __name__ == '__main__':
    main()
