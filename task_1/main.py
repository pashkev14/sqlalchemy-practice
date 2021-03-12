from flask import Flask
from task_1.data import db_session
from task_1.data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/jobs.db')
    db_sess = db_session.create_session()
    user, user2, user3, user4 = User(), User(), User(), User()
    user_values = ["Scott", "Ridley", "21", "captain", "research engineer", "module_1", "scott_chief@mars.org"]
    user2_values = ["Trelawny", "Squire", "25", "executive", "science", "module_2", "trelala@mars.org"]
    user3_values = ["Livsey", "Doctor", "30", "master", "construction", "module_1", "hahahahaha@mars.org"]
    user4_values = ["Herrington", "Billy", "45", "slave", "digging", "module_2", "dgmstr@mars.org"]
    user.surname, user.name, user.age, user.position, user.speciality, user.address, user.email = user_values
    user2.surname, user2.name, user2.age, user2.position, user2.speciality, user2.address, user2.email = user2_values
    user3.surname, user3.name, user3.age, user3.position, user3.speciality, user3.address, user3.email = user3_values
    user4.surname, user4.name, user4.age, user4.position, user4.speciality, user4.address, user4.email = user4_values
    db_sess.add(user)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(user4)
    db_sess.commit()


if __name__ == '__main__':
    main()
