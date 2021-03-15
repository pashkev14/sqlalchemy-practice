from flask import Flask, render_template, url_for
from task_3.data.jobs import Jobs
from task_3.data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def show_db():
    db_session.global_init("db/jobs.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    css = url_for('static', filename='css/base.css')
    return render_template("log.html", css=css, jobs=jobs)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
