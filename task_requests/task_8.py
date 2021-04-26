def main():
    file = input()
    global_init(file)
    db_sess = create_session()
    answer = []
    depart = db_sess.query(Department).filter(Department.id == 1).first()
    members = depart.members.split(', ')
    for i in members:
        hours = 0
        all_jobs = db_sess.query(Jobs).all()
        for j in all_jobs:
            if i in j.collaborators.split(', '):
                hours += j.work_size
        if hours > 25:
            user = db_sess.query(User).filter(User.id == int(i)).first()
            if f"{user.name} {user.surname}" not in answer:
                answer.append(f"{user.name} {user.surname}")
    print('\n'.join(answer))
