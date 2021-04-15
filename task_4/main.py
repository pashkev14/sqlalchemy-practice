import datetime
from flask import Flask, render_template, url_for
from werkzeug.utils import redirect
from task_4.data.users import User
from task_4.data import db_session
from task_4.registerform import RegisterForm
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    css = url_for('static', filename='css/base.css')
    form = RegisterForm()
    if form.validate_on_submit():
        db_session.global_init("db/jobs.db")
        db_sess = db_session.create_session()
        user = User()
        user.surname = form.surname_field.data
        user.name = form.name_field.data
        user.age = form.age_field.data
        user.position = form.position_field.data
        user.speciality = form.speciality_field.data
        user.address = form.address_field.data
        user.email = form.email_field.data
        user.hashed_password = generate_password_hash(form.password_field.data)
        user.modified_date = datetime.datetime.now()
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', css=css, form=form)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
