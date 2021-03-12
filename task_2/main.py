from flask import Flask
from task_2.data import db_session
from task_2.data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/jobs.db')
    db_sess = db_session.create_session()
    job = Jobs()
    job_values = ["1", "deployment of residential modules 1 and 2", "15", "2, 3", datetime.datetime.now(), False]
    job.team_leader, job.job, job.work_size, job.collaborators, job.start_date, job.is_finished = job_values
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()
