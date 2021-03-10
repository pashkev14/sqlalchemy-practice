from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/jobs.db')
    user, user2, user3, user4 = User(), User(), User(), User()
    user_values = ["Scott", "Ridley", "21", "captain", "research engineer", "module_1", "scott_chief@mars.org"]
    user2_values = ["Trelawny", "Squire", "25", "executive", "science", "module_2", "trelala@mars.org" ]
    user3_values = ["Livsey"]
    user4_values = []
    user.surname, user.name, user.age, user.position, user.speciality, user.address, user.email = user_values




if __name__ == '__main__':
    main()
